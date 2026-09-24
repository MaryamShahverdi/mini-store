import sys

#Product 
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name: str = name
        self.price: float = price
        self.stock: int = stock

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


#Store 
class Store:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, name: str, price: float, stock: int):
    
        for p in self.products:
            if p.name.lower() == name.lower():
                p.stock += stock
                return
        self.products.append(Product(name, price, stock))

    def list_products(self):
        for idx, p in enumerate(self.products, 1):
            print(f"[{idx}] {p}")

    def find_product(self, name: str) -> Product:
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None


#CartItem
class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity


#Cart
class Cart:
    def __init__(self):
        self.items: list[CartItem] = []

    def add_to_cart(self, product: Product, quantity: int):
        if quantity > product.stock:
            print(f" Not enough stock! Only {product.stock} available.")
            return False
        
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                product.stock -= quantity
                return True
        
        self.items.append(CartItem(product, quantity))
        product.stock -= quantity
        return True

    def remove_from_cart(self, product_name: str):
        for item in self.items:
            if item.product.name.lower() == product_name.lower():
                item.product.stock += item.quantity
                self.items.remove(item)
                return True
        return False

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        
        print("Your cart:")
        for item in self.items:
            cost = item.product.price * item.quantity
            print(f" - {item.product.name} x{item.quantity} - ${cost:.2f}")
        print(f"Total: ${self.total_price():.2f}")

    def total_price(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items)

class MiniStoreApp:
    def __init__(self):
        self.store = Store()
        self.admin_user = "admin"
        self.admin_pass = "1234"

    def run(self):
        while True:
            print("\n=================================")
            print(" MINI STORE MANAGEMENT SYSTEM ")
            print("=================================")
            print("\n Welcome! Please select your role:")
            print("1. Store Manager")
            print("2. Customer")
            print("3. Exit Program")
            
            choice = input("Enter choice: ")

            if choice == "1":
                self.handle_manager()
            elif choice == "2":
                self.handle_customer()
            elif choice == "3":
                print("\n Goodbye! See you next time.")
                break

    def handle_manager(self):
        print("\n--------------------------------")
        print(" Store Manager Login")
        print("--------------------------------")
        user = input("Username: ")
        pw = input("Password: ")

        if user == self.admin_user and pw == self.admin_pass:
            print("\n Login successful! Welcome, Manager.")
            self.manager_panel()
        else:
            print("\n Login failed! Please try again or return to main menu.")

    def manager_panel(self):
        while True:
            print("\n--------------------------------")
            print("  Add Products")
            print("--------------------------------")
            name = input("Enter product name (or 'done' to finish): ")
            if name.lower() == 'done':
                print("Returning to main menu...")
                break
            
            try:
                price = float(input("Enter product price: "))
                stock = int(input("Enter product stock quantity: "))
                self.store.add_product(name, price, stock)
                print(f" Product added: {name} - ${price:.2f} (Stock: {stock})")
            except ValueError:
                print(" Invalid input! Please enter numbers for price and stock.")

    def handle_customer(self):
        cart = Cart()
        while True:
            print("\n--------------------")
            print(" CUSTOMER PORTAL")
            print("--------------------")
            print("Hello, dear customer!")
            print("Available products:")
            self.store.list_products()
            
            print("\nWhat would you like to do?")
            print("1. Add item to cart")
            print("2. Remove item from cart")
            print("3. View cart")
            print("4. Checkout")
            print("5. Return to main menu")
            
            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter product name: ")
                p = self.store.find_product(name)
                if p:
                    try:
                        qty = int(input("Enter quantity: "))
                        if cart.add_to_cart(p, qty):
                            print(f" Added {qty} x {p.name} to cart.")
                    except ValueError:
                        print(" Invalid quantity.")
                else:
                    print(" Product not found.")

            elif choice == "2":
                name = input("Enter product name to remove: ")
                if cart.remove_from_cart(name):
                    print(f" Removed {name} from cart.")
                else:
                    print(" Item not found in cart.")

            elif choice == "3":
                cart.view_cart()

            elif choice == "4":
                if not cart.items:
                    print(" Your cart is empty.")
                    continue
                print("\n Final Checkout:")
                cart.view_cart()
                print(" Thank you for shopping with us!")
                break 

            elif choice == "5":
                for item in cart.items:
                    item.product.stock += item.quantity
                print("Returning to main menu...")
                break

if __name__ == "__main__":
    MiniStoreApp().run()
