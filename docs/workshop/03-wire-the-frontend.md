# 03 — Wire the Frontend

**Time:** ~20 minutes  
**Features:** Inline completions, chat, `/fix`, component generation, skills

**Learning goals:**
- See how skills and instructions guide React/TypeScript component generation
- Practice using inline completions for JSX and hooks
- Observe how Copilot understands the data flow from types + instructions
- Learn how to iterate and refine generated components using chat commands

> **Note:** The frontend stubs demonstrate how Copilot generates production-shaped React components. You'll build them to understand how Copilot handles UI, state, and API integration — skills applicable to any React project.

---

## 🛠️ Activate the frontend-engineer skill

The **`frontend-engineer`** skill loads React, TypeScript, Tailwind, and API service conventions automatically. In Copilot Chat, try:

```
Use the frontend-engineer skill to help me implement ProductCard.tsx
```

Or just start asking about components, hooks, TypeScript types, or Tailwind — and the skill will kick in on its own.

> 💡 **What this teaches:** Skills enable role-specific personas. This skill makes Copilot think like a React specialist — it knows component patterns, hooks conventions, and type safety rules without manual re-explanation.

---

## The frontend at a glance

```
frontend/src/
├── services/api.ts        ← 🔧 API calls (partially stubbed)
├── components/
│   ├── Header.tsx         ← ✅ Complete
│   ├── ProductCard.tsx    ← 🔧 Stub — you'll implement this
│   └── Cart.tsx           ← 🔧 Stub — you'll implement this
├── pages/
│   ├── ProductsPage.tsx   ← 🔧 Stub — you'll implement this
│   └── CheckoutPage.tsx   ← 🔧 Stub — you'll implement this
└── types/index.ts         ← ✅ All types are defined
```

---

## Step 1 — Complete `api.ts`

Open `frontend/src/services/api.ts`.

`fetchProducts()` is already implemented. Complete `createOrder()`:

**Inline approach:** Place your cursor at the end of the TODO comment inside `createOrder` and press `Tab` / `Alt+\`.

**Chat approach:**
```
Implement createOrder: POST to ${BASE_URL}/orders with the request as JSON body, 
check response.ok, return response.json() as Order
```

Also implement `fetchProduct(id)` while you're here.

---

## Step 2 — Implement `ProductCard.tsx`

Open `frontend/src/components/ProductCard.tsx`.

Delete the placeholder `<div>` and type `return (` — then wait for Copilot to suggest the full JSX.

If it doesn't trigger, ask in Chat:
```
Generate JSX for a product card that shows:
- product image (img tag with imageUrl)
- product name (h3)
- category (small badge)
- price formatted as currency (€)
- stock indicator (green if stock > 0, red if 0)
- "Add to Cart" button, disabled when stock === 0
Call onAddToCart(product) on click.
```

Review the suggestion, adjust styling if desired, and save.

---

## Step 3 — Implement `ProductsPage.tsx`

Open `frontend/src/pages/ProductsPage.tsx`. The state variables and handlers are declared but the products aren't fetched yet (notice `void fetchProducts` at line 37 — that's the hint).

In Chat:
```
@workspace Complete ProductsPage: 
add a useEffect that calls fetchProducts() on mount, 
set loading true before the call and false after,
catch errors and set the error state
```

Copilot should generate the `useEffect` referencing the existing state variables (`setProducts`, `setLoading`, `setError` — which you may need to add setters for).

> 💡 Tip: If TypeScript complains about `const [products]` missing a setter, Copilot's `/fix` will add `setProducts` automatically.

---

## Step 4 — Implement `Cart.tsx`

Open `frontend/src/components/Cart.tsx`. In Chat:

```
Implement the Cart component:
- List each CartItem with product name, quantity, and line total (price × quantity)
- Show a grand total at the bottom
- Each item has a remove button that calls onRemoveItem(item.product.id)
- A "Checkout" button that calls onCheckout()
- If cart is empty, show a friendly "Your cart is empty" message
```

---

## Step 5 — Implement `CheckoutPage.tsx`

Open `frontend/src/pages/CheckoutPage.tsx`. In Chat:

```
@workspace Implement CheckoutPage:
- Form with customerName and customerEmail fields
- On submit, call createOrder() from services/api with the cart items
- Show a success message with the returned order ID
- Show an error message if the request fails
- The cart items should come from... where? 
  Ask Copilot how to share state between pages in this app.
```

> This last part is intentionally open-ended. See if Copilot suggests lifting state to `App.tsx`, using React Context, or another approach. This is a great discussion point about state management trade-offs.

---

## Step 6 — Test the full flow

1. In the Codespaces **Ports** tab, find port **5173** and select **Open in Browser**. Use the forwarded address that opens as `<frontend-codespace-url>` for the webshop.
2. Products should load from the backend
3. Add items to cart
4. Click Checkout
5. Fill in name + email, submit
6. Verify the order in the H2 console: `SELECT * FROM orders;`

---

## Step 7 — Validate Your Components with a Custom Prompt

Now that you've built ProductCard, Cart, and CheckoutPage, let's enforce design standards. Select `ProductCard.tsx` and paste this one-time prompt into Copilot Chat:

```
Review this ProductCard component against the designer skill:
1. Does it use Tailwind utility classes (no inline styles)?
2. Are all interactive elements keyboard-accessible?
3. Does the "Add to Cart" button have a focus ring?
4. Is there a disabled state with proper styling when stock === 0?
5. Does the component use the project color palette (violet, emerald, rose)?
6. Are all images required to have alt text?

Suggest specific CSS class changes if needed.
```

Make any improvements it suggests.

> 💡 **Key insight:** This detailed review prompt would be useful for every component. In [Part 04](./04-agents-and-skills.md), you'll save it as a reusable file.

---

## Copilot prompts to try

| Prompt | What it demonstrates |
|--------|----------------------|
| Type `return (` in a stub component | Inline JSX generation |
| `@workspace how does data flow from the API to the UI?` | Cross-file tracing |
| `/explain` on a React hook you don't recognise | Learning aid |
| `/fix` on TypeScript errors | Error recovery |
| `Format price as EUR currency in TypeScript` | Targeted snippets |
| Custom component review request (Step 7) | **Prompting for quality** ⭐ |

---

**Next:** [Part 4 — Agents & Skills →](./04-agents-and-skills.md)
