#!/usr/bin/env python3
"""Regenerate the checklist tables in references/ from official OWASP sources.

Hand-written sections are preserved: everything from "## Key PASS/FAIL Patterns" onward
(ASVS, AISVS) and each "### What to check" block (MASVS). Review the diff afterwards and
update version numbers and counts in SKILL.md, level-selection.md and assessment-rules.md.

  asvs  <ASVS csv> [ver]  e.g. OWASP_Application_Security_Verification_Standard_5.0.0_en.csv
  aisvs <AISVS en dir>    e.g. AISVS/1.0/en
  masvs <masvs repo dir>  containing OWASP_MASVS.yaml and controls/
"""
import csv, glob, os, re, sys

REF = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references')

def anchor(h):
    return re.sub(r'\s+', '-', re.sub(r'[^a-z0-9\s-]', '', h.lower())).strip('-')

def clean(d):
    d = re.sub(r'^Verify that[,\s]+', '', ' '.join(d.split()), flags=re.I)
    return (d[0].upper() + d[1:]).replace('|', '\\|')

def keep_tail(path, marker='\n## Key PASS/FAIL Patterns\n'):
    if not os.path.exists(path):
        return ''
    old = open(path, encoding='utf-8').read()
    i = old.find(marker)
    return old[i:].strip() if i >= 0 else ''

def write_tables(name, title, load, rows, cite, grep_example):
    """rows: list of dict(ch, ch_name, sec, sec_name, id, desc, level)"""
    path = os.path.join(REF, name + '.md')
    tail = keep_tail(path)
    chs = list(dict.fromkeys(r['ch'] for r in rows))
    c = {l: sum(r['level'] == l for r in rows) for l in '123'}
    heads = []
    for ch in chs:
        cr = [r for r in rows if r['ch'] == ch]
        heads.append(f"{ch} {cr[0]['ch_name']} ({len(cr)} reqs, {sum(r['level'] == '1' for r in cr)} at L1)")
    out = [f"# {title}: {', '.join(chs)}", '', f"Load when: {load}",
           f"Total: {len(rows)} requirements (L1: {c['1']}, L2: {c['2']}, L3: {c['3']}). Levels are cumulative: an L2 assessment checks every row marked 1 or 2.",
           cite, f"Look up one row: `grep -F \"| {grep_example} |\" references/<this file>`", '', '## Contents', '']
    out += [f"- [{h}](#{anchor(h)})" for h in heads + (['Key PASS/FAIL Patterns'] if tail else [])] + ['']
    for ch, h in zip(chs, heads):
        out += ['---', '', f"## {h}"]
        sec = None
        for r in rows:
            if r['ch'] != ch:
                continue
            if r['sec'] != sec:
                sec = r['sec']
                out += ['', f"### {sec} {r['sec_name']}", '', '| ID | L | Requirement |', '|---|---|---|']
            out.append(f"| {r['id']} | {r['level']} | {clean(r['desc'])} |")
        out.append('')
    if tail:
        out += ['---', '', tail]
    open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(f'{name}: {len(rows)} requirements')

ASVS_GROUPS = [
    ('asvs-input', ['V1', 'V2'], 'Always when ASVS applies'),
    ('asvs-auth', ['V6', 'V7', 'V8'], 'Always when ASVS applies'),
    ('asvs-web-api', ['V3', 'V4', 'V5'], 'Full Assessment; Quick Scan when a browser UI or file handling is present'),
    ('asvs-tokens-oauth', ['V9', 'V10'], 'Full Assessment (rows N/A when no tokens, OAuth, or OIDC)'),
    ('asvs-infra', ['V11', 'V12', 'V13'], 'Always when ASVS applies'),
    ('asvs-data-quality', ['V14', 'V15', 'V16', 'V17'], 'Full Assessment (V17 rows N/A without WebRTC)'),
]
AISVS_GROUPS = [
    ('aisvs-core', ['C2', 'C5', 'C7', 'C12'], 'Always when AISVS applies (any LLM/ML feature)'),
    ('aisvs-ml-pipeline', ['C1', 'C3', 'C4', 'C6', 'C11'], 'Full Assessment (rows N/A when the code does not train, host, package, or download models)'),
    ('aisvs-rag-agents', ['C8', 'C9', 'C10'], 'Quick Scan when RAG, agents/tool calling, or MCP are present; always in Full Assessment'),
]

def asvs(src, ver=None):
    rows = [dict(ch=r['chapter_id'], ch_name=r['chapter_name'], sec=r['section_id'], sec_name=r['section_name'],
                 id=r['req_id'], desc=r['req_description'], level=r['L'].strip())
            for r in csv.DictReader(open(src, encoding='utf-8'))]
    m = re.search(r'(\d+\.\d+\.\d+)', os.path.basename(src))
    ver = ver or (m and m.group(1))
    if not ver:
        sys.exit('ASVS version not in file name; pass it as a third argument, e.g. 5.0.0')
    for name, chs, load in ASVS_GROUPS:
        write_tables(name, f'ASVS {ver}', load, [r for r in rows if r['ch'] in chs],
                     f'Requirement text is verbatim from the official ASVS {ver} CSV with the leading "Verify that" removed. Cite IDs in reports as v{ver}-<number> (V1.2.4 -> v{ver}-1.2.4).',
                     f"{chs[0]}.1.1")

def aisvs(src):
    rows = []
    for f in sorted(glob.glob(os.path.join(src, '0x10-C*.md'))):
        t = open(f, encoding='utf-8').read()
        ch = re.search(r'^# (C\d+) (.+)$', t, re.M)
        sec = None
        for line in t.splitlines():
            m = re.match(r'^## (C\d+\.\d+) (.+)$', line)
            if m:
                sec = m.groups(); continue
            m = re.match(r'^\|\s*\*\*(\d+\.\d+\.\d+)\*\*\s*\|\s*(.+?)\s*\|\s*(\d)\s*\|\s*$', line)
            if m:
                rows.append(dict(ch=ch.group(1), ch_name=ch.group(2).strip(), sec=sec[0], sec_name=sec[1].strip(),
                                 id='C' + m.group(1), desc=m.group(2).replace('**', ''), level=m.group(3)))
    for name, chs, load in AISVS_GROUPS:
        write_tables(name, 'AISVS 1.0', load, [r for r in rows if r['ch'] in chs],
                     'Requirement text is verbatim from the locked AISVS v1.0 source (1.0/en) with the leading "Verify that" removed. Cite IDs as v1.0-<id> (C2.1.3 -> v1.0-C2.1.3).',
                     f"{chs[0]}.1.1")

def masvs(src):
    import yaml
    d = yaml.safe_load(open(os.path.join(src, 'OWASP_MASVS.yaml'), encoding='utf-8'))
    path = os.path.join(REF, 'masvs-checklist.md')
    old = open(path, encoding='utf-8').read()
    head = old[:old.index('## Contents')]
    checks = dict(re.findall(r'^## (MASVS-[A-Z]+) .*?\n### What to check\n\n(.*?)(?=\n---\n|\Z)', old, re.M | re.S))
    def desc(cid):
        t = open(os.path.join(src, 'controls', cid + '.md'), encoding='utf-8').read()
        m = re.search(r'## Description\s*\n(.+)', t, re.S)
        return ' '.join(m.group(1).split()).replace('|', '/') if m else ''
    out = [head.rstrip(), '', '## Contents', '']
    for g in d['groups']:
        h = f"{g['id']} {g['title']} ({len(g['controls'])} controls)"
        out.append(f"- [{h}](#{anchor(h)})")
    out.append('')
    for g in d['groups']:
        out += ['---', '', f"## {g['id']} {g['title']} ({len(g['controls'])} controls)", '', '| ID | Control | What it covers |', '|---|---|---|']
        out += [f"| {c['id']} | {c['statement']} | {desc(c['id'])} |" for c in g['controls']]
        out += ['', '### What to check', '', checks.get(g['id'], 'TODO: write checks for this group').strip(), '']
    open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(f"masvs-checklist: {sum(len(g['controls']) for g in d['groups'])} controls")

if __name__ == '__main__':
    if len(sys.argv) not in (3, 4) or sys.argv[1] not in ('asvs', 'aisvs', 'masvs'):
        sys.exit(__doc__)
    if sys.argv[1] == 'asvs':
        asvs(*sys.argv[2:])
    else:
        {'aisvs': aisvs, 'masvs': masvs}[sys.argv[1]](sys.argv[2])
