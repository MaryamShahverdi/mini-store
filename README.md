## Mini Store 🛒

A simple console-based store management system built with Python and object-oriented programming. It supports two roles — a **Store Manager** who adds products, and a **Customer** who browses, adds items to a cart, and checks out.

## ✨ Features

- 👨‍💼 **Manager mode** (login required) — add new products with name, price, and stock quantity
- 🛍️ **Customer mode** — browse available products, add/remove items from a shopping cart, view the cart total, and checkout
- 📦 Automatic stock management — stock decreases when items are added to a cart and is restored if items are removed or the customer leaves without checking out
- 🔁 Duplicate product handling — adding a product that already exists increases its stock instead of creating a duplicate

## 🏗️ Structure

- `Product` — represents a single product (name, price, stock)
- `Store` — holds and manages the list of products
- `CartItem` / `Cart` — represents a customer's shopping cart and its contents
- `MiniStoreApp` — the main application loop that ties everything together

## 🚀 Usage

```bash
python mini_store.py
```

You'll be asked to choose a role:
1. **Store Manager** (default login: `admin` / `1234`)
2. **Customer**
3. **Exit**

## 💡 Example

```
=================================
 MINI STORE MANAGEMENT SYSTEM
=================================

Welcome! Please select your role:
1. Store Manager
2. Customer
3. Exit Program
Enter choice: 2

CUSTOMER PORTAL
Available products:
[1] Watch - $120.00 (Stock: 5)

What would you like to do?
1. Add item to cart
2. Remove item from cart
3. View cart
4. Checkout
5. Return to main menu
```
