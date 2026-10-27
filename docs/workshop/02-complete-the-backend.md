# 02 — Complete the Backend

**Time:** ~20 minutes  
**Features:** Inline completions, `/explain`, `/fix`, `@workspace`, skills

**Learning goals:**
- See how `copilot-instructions.md` and skills guide Copilot's code generation
- Practice using Copilot chat commands (`/explain`, `/fix`) for code understanding and debugging
- Observe how `@workspace` enables cross-file understanding
- Understand how Copilot fills in stubs when context is clear

> **Note:** The backend stubs serve as a realistic vehicle to demonstrate Copilot's capabilities. You'll complete them using Copilot — not to "finish the webshop," but to learn how Copilot assists with full-stack development.

---

## 🛠️ What are Skills? (`.github/skills/`)

A **Skill** is a folder located in `.github/skills/` containing a `SKILL.md` file that packages specialized domain knowledge, architectural patterns, and coding conventions for a specific topic or role.

- **`copilot-instructions.md`** = Always active repository-wide baseline rules.
- **Skills (`.github/skills/`)** = Modular, on-demand domain expertise. Copilot loads a skill automatically when your prompt or active file matches the skill's description, or when you explicitly ask Copilot to use it.

---

## 🛠️ Activate the backend-engineer skill

The **`backend-engineer`** skill (`.github/skills/backend-engineer/SKILL.md`) loads deeper Kotlin, Spring Boot, and JPA conventions automatically. In Copilot Chat, try:

```
Use the backend-engineer skill to explain how the service layer works in this project.
```

Or just start asking about controllers, services, repositories, or Kotlin — and the skill will kick in on its own.

> 💡 **What this teaches:** Skills are a way to package domain knowledge so Copilot can adopt the right persona for the task. Without manually re-explaining, Copilot understands your backend architecture, naming rules, and patterns.

---

## The backend at a glance

```
backend/src/main/kotlin/com/webshop/
├── controller/   ← HTTP layer (REST endpoints)
├── service/      ← Business logic
├── repository/   ← Database access (JPA)
└── model/        ← Data classes (entities)
```

The **models** and **repositories** are complete. The **services** and **controllers** have stubs for you to fill in.

---

## Step 1 — Understand the data layer with `/explain`

Open `backend/src/main/kotlin/com/webshop/repository/ProductRepository.kt`.

Select the whole file, open Copilot Chat, and type:
```
/explain
```

Copilot will explain what `JpaRepository` gives you for free, what `findByCategory` and `findByNameContainingIgnoreCase` do, and how Spring generates SQL from the method names.

---

## Step 2 — Use `@workspace` for cross-file understanding

In Copilot Chat, ask:

```
@workspace How does the Product entity map to the H2 database? Trace from the model to the SQL.
```

Watch Copilot trace `Product.kt` → `ProductRepository.kt` → `application.yml` → `data.sql` in a single answer.

---

## Step 3 — Implement GET /api/orders

Open `OrderController.kt`. Find the `getAllOrders()` method with the TODO comment.

**Option A — Inline completion:**  
Delete the TODO comment and the `return` line, then type `return ResponseEntity.ok(` and let Copilot complete it.

**Option B — Chat:**  
Select the method body, then in Copilot Chat type:
```
Implement this to call orderService.getAllOrders() and return 200 OK
```

Do the same for `getOrderById()`.

---

## Step 4 — Implement POST /api/orders

This is the most complex stub. The `createOrder` method needs to:
1. Map `CreateOrderRequest.items` to something the service understands
2. Call `orderService.createOrder(...)`
3. Return `201 Created` with the saved order

In Copilot Chat, with `OrderController.kt` open, ask:
```
@workspace Implement createOrder in OrderController. 
Map the request items to the service, return 201 Created.
```

Review what Copilot generates — it may also suggest completing `OrderService.kt`. Accept the changes.

> **Import note:** `CreateOrderItemCommand` is defined in `OrderService.kt`, so it needs to be imported in `OrderController.kt`. If you see a red squiggle on that type, use `/fix` or accept the import Copilot adds automatically.

---

## Step 5 — Complete OrderService

Open `OrderService.kt` and look at the `createOrder` stub.

Place your cursor inside the function body and press `Tab` or `Alt+\` to trigger an inline suggestion. If nothing appears, use Chat:

```
Implement createOrder: look up each product, reduce stock, create an Order with OrderItems, save and return it
```

> ⚠️ If Copilot generates code that doesn't compile, select the error and use `/fix`.

---

## Step 6 — Verify in H2 console

1. Make sure the backend is running (`./gradlew bootRun`)
2. In the Codespaces **Ports** tab, find port **8080** and copy or open its forwarded address. Open `<backend-codespace-url>/h2-console` in your browser, replacing the placeholder with that address.
3. JDBC URL: `jdbc:h2:mem:webshopdb`, User: `sa`, Password: *(empty)*
4. Run: `SELECT * FROM PRODUCT;` — you should see 10 rows
5. Use `curl` in the Codespaces terminal or open `<backend-codespace-url>/api/products` in your browser to test. Replace the placeholder with the forwarded address for port **8080**.

```bash
curl http://localhost:8080/api/products
```

```bash
curl -X POST http://localhost:8080/api/orders \
  -H "Content-Type: application/json" \
  -d '{"customerName":"Alice","customerEmail":"alice@example.com","items":[{"productId":1,"quantity":2}]}'
```

---

## Step 7 — Write Tests with a Custom Prompt

Now that the backend is working, let's test it. In Copilot Chat, with `ProductControllerTest.kt` open, paste this one-time prompt:

```
@backend-engineer Generate a test for POST /api/orders using MockMvc that:
1. Mocks orderService.createOrder() to return a valid Order
2. Sends a POST request with valid customer name, email, and items
3. Asserts the response status is 201 Created
4. Asserts the response JSON includes order.id, order.customerName, and order.total
5. Also includes an error case where the service throws an exception
```

Review the generated test and run it:
```bash
cd backend && ./gradlew test
```

> 💡 **Key insight:** You had to write and copy a detailed prompt. In [Part 04](./04-agents-and-skills.md), you'll turn this kind of prompt into a reusable file.

---

## Copilot prompts to try

| Prompt | What it demonstrates |
|--------|----------------------|
| `/explain` on `ProductRepository.kt` | Understanding unfamiliar code |
| `@workspace How does CORS work here?` | Cross-file awareness |
| `/fix` on a compile error | Error recovery |
| `Generate a curl command to test POST /api/orders` | Dev productivity |
| Custom test-generation prompt (Step 7) | **Prompting for quality** ⭐ |

---

**Next:** [Part 3 — Wire the Frontend →](./03-wire-the-frontend.md)
