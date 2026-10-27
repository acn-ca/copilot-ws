#!/usr/bin/env python3
"""Build and tally the per-requirement working table for an OWASP assessment.

init:  python3 scripts/req_table.py init --level 2 --out table.tsv references/asvs-input.md references/asvs-auth.md ...
       Writes one TSV row per requirement at or below --level (MASVS rows have no level and are
       always included). Columns: id, level, chapter, requirement, status, evidence.
       Use --chapters V1,V2,V6 to restrict to chapters (Quick Scan).
tally: python3 scripts/req_table.py tally table.tsv
       Validates statuses, flags empty rows, prints per-chapter and total counts plus the score
       Pass / (Pass + Fail + Partial), as a Markdown table ready to paste into the report.
set:   python3 scripts/req_table.py set table.tsv V1.2.4 PASS "src/db.kt:40 parameterized"
       Sets status and evidence for one row (ID as in the table), keeping TSV quoting intact.
report: python3 scripts/req_table.py report table.tsv [--asvs-version 5.0.0] [--aisvs-version 1.0]
       Prints the requirement-results table with versioned IDs (v5.0.0-1.2.4, v1.0-C2.1.3,
       MASVS-STORAGE-1), requirement text cut to its first ~80 characters, level, status and
       evidence, grouped under one heading per chapter. Paste it into the report.
"""
import argparse, csv, re, sys
from collections import OrderedDict

ROW = re.compile(r'^\| (V\d+\.\d+\.\d+|C\d+\.\d+\.\d+) \| (\d) \| (.+) \|\s*$')
MROW = re.compile(r'^\| (MASVS-[A-Z]+-\d) \| (.+?) \| .* \|\s*$')
STATUSES = ['PASS', 'FAIL', 'PARTIAL', 'NOT VERIFIED', 'N/A']

def chapter(rid):
    if rid.startswith('MASVS-'):
        return rid.rsplit('-', 1)[0]
    return rid.split('.')[0]

def init(a):
    chapters = set(a.chapters.split(',')) if a.chapters else None
    rows = []
    for path in a.files:
        for line in open(path, encoding='utf-8'):
            m = ROW.match(line)
            if m:
                rid, lvl, text = m.groups()
                if int(lvl) > a.level:
                    continue
            else:
                m = MROW.match(line)
                if not m:
                    continue
                rid, text = m.groups(); lvl = '-'
            if chapters and chapter(rid) not in chapters:
                continue
            rows.append([rid, lvl, chapter(rid), text.replace('\t', ' '), '', ''])
    with open(a.out, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['id', 'level', 'chapter', 'requirement', 'status', 'evidence'])
        w.writerows(rows)
    print(f'{len(rows)} requirements written to {a.out}')

def tally(a):
    counts, problems = OrderedDict(), []
    with open(a.table, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            s = r['status'].strip().upper().replace('NV', 'NOT VERIFIED').replace('NA', 'N/A')
            if s not in STATUSES:
                problems.append(f"{r['id']}: status '{r['status']}'")
                continue
            if s != 'PASS' and s != 'N/A' and not r['evidence'].strip():
                problems.append(f"{r['id']}: {s} without evidence")
            if s == 'N/A' and not r['evidence'].strip():
                problems.append(f"{r['id']}: N/A without reason")
            c = counts.setdefault(r['chapter'], dict.fromkeys(STATUSES, 0))
            c[s] += 1
    total = dict.fromkeys(STATUSES, 0)
    print('| Chapter | Pass | Fail | Partial | NV | N/A | Score |\n|---|---|---|---|---|---|---|')
    def line(name, c):
        scored = c['PASS'] + c['FAIL'] + c['PARTIAL']
        score = f"{100 * c['PASS'] / scored:.0f}%" if scored else '-'
        print(f"| {name} | {c['PASS']} | {c['FAIL']} | {c['PARTIAL']} | {c['NOT VERIFIED']} | {c['N/A']} | {score} |")
    def order(ch):
        m = re.match(r'([A-Z]+)(\d+)$', ch)
        return (0, m.group(1), int(m.group(2))) if m else (1, ch, 0)
    keys = list(counts) if all(k.startswith('MASVS-') for k in counts) else sorted(counts, key=order)
    for ch in keys:
        c = counts[ch]
        line(ch, c)
        for k in STATUSES:
            total[k] += c[k]
    line(f'Total ({sum(total.values())})', total)
    if problems:
        print('\nProblems to fix before reporting:', *problems, sep='\n- ')
        sys.exit(1)

def short(text, n=80):
    text = text.replace('\\|', '/').replace('|', '/')
    return text if len(text) <= n else text[:n].rsplit(' ', 1)[0] + '...'

def versioned(rid, a):
    if rid.startswith('V'):
        return f'v{a.asvs_version}-{rid[1:]}'
    if rid.startswith('C'):
        return f'v{a.aisvs_version}-{rid}'
    return rid

def set_row(a):
    status = a.status.strip().upper()
    if status not in STATUSES:
        sys.exit(f"status must be one of {', '.join(STATUSES)}")
    with open(a.table, encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f, delimiter='\t'))
    hits = [r for r in rows[1:] if r[0] == a.id]
    if not hits:
        sys.exit(f'{a.id} not in {a.table}')
    hits[0][4], hits[0][5] = status, ' '.join(a.evidence.split())
    with open(a.table, 'w', encoding='utf-8', newline='') as f:
        csv.writer(f, delimiter='\t').writerows(rows)
    print(f'{a.id}: {status}')

def report(a):
    with open(a.table, encoding='utf-8') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    current = None
    for r in rows:
        if r['chapter'] != current:
            current = r['chapter']
            print(f"\n#### {current}\n\n| Req ID | Requirement | L / tier | Status | Evidence / reason |\n|---|---|---|---|---|")
        ev = r['evidence'].replace('|', '/').strip()
        print(f"| {versioned(r['id'], a)} | {short(r['requirement'])} | {r['level']} | {r['status'].strip()} | {ev} |")

p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sp = p.add_subparsers(dest='cmd', required=True)
i = sp.add_parser('init'); i.add_argument('--level', type=int, default=1); i.add_argument('--out', required=True)
i.add_argument('--chapters'); i.add_argument('files', nargs='+')
t = sp.add_parser('tally'); t.add_argument('table')
st = sp.add_parser('set'); st.add_argument('table'); st.add_argument('id'); st.add_argument('status')
st.add_argument('evidence', nargs='?', default='')
r = sp.add_parser('report'); r.add_argument('table')
r.add_argument('--asvs-version', default='5.0.0'); r.add_argument('--aisvs-version', default='1.0')
a = p.parse_args()
{'init': init, 'tally': tally, 'set': set_row, 'report': report}[a.cmd](a)
