import json
import os

"""import unittest

import unittest
from inventory import Product"""


"""class TestProduct(unittest.TestCase):

    def test_product_details(self):
        product = Product(101, "Laptop", 50000, 5)

        self.assertEqual(product.product_id, 101)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 50000)
        self.assertEqual(product.quantity, 5)
"""

"""if __name__ == "__main__":
    unittest.main()

class TestProduct(unittest.TestCase):
    def test_get_price(self):
        product = Product("Laptop", 50000)
        self.assertEqual(product.get_price(), 50000)

if __name__ == "__main__":
    unittest.main()"""

class Product: 
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name 
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(
            f"ID: {self.product_id} | Name: {self.name} | "
            f"Price: ₹{self.price:.2f} | Stock: {self.quantity}"
        )

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

class Inventory: 
    def __init__(self, filename="inventory.json"):
        self.products = {} 
        self.filename = filename
        self.load_from_file()

    def add_product(self, product):
        if product.product_id in self.products:
            print("A product with this ID already exists.")
            return

        if product.price < 0 or product.quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        self.products[product.product_id] = product
        self.save_to_file()
        print(f"{product.name} added successfully.")

    def display_products(self):
        if not self.products:
            print("Inventory is empty.")
            return

        print("\n--- INVENTORY ---")
        for product in self.products.values():
            product.display_info()
       
    def find_product(self, product_id):
        return self.products.get(product_id)

    def restock_product(self, product_id, quantity):
        product = self.find_product(product_id)

        if product is None:
            print("Product not found.")
            return

        if quantity <= 0:
            print("Restock quantity must be greater than zero.")
            return

        product.quantity += quantity
        self.save_to_file()
        print(
            f"Stock updated. {product.name} now has "
            f"{product.quantity} units."
        )

    def sell_product(self, product_id, quantity):
        product = self.find_product(product_id)

        if product is None:
            print("Product not found.")
            return

        if quantity <= 0:
            print("Sale quantity must be greater than zero.")
            return

        if quantity > product.quantity:
            print(f"Not enough stock. Available quantity: {product.quantity}")
            return

        product.quantity -= quantity
        subtotal = product.price * quantity
        self.save_to_file()

        print("\n--- SALE RECEIPT ---")
        print(f"Product: {product.name}")
        print(f"Quantity sold: {quantity}")
        print(f"Unit price: ₹{product.price:.2f}")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Remaining stock: {product.quantity}")

    def remove_product(self, product_id):
        product = self.products.get(product_id)

        if product is None:
            print("Product not found.")
            return

        del self.products[product_id]
        self.save_to_file()
        print(f"{product.name} removed from inventory.")

    def save_to_file(self):
        data = [product.to_dict() for product in self.products.values()]

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except OSError as error:
            print(f"Could not save inventory: {error}")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                print("Invalid file format")
                return

            for item in data:

                if not isinstance(item, dict):
                    print("Invalid product record")
                    continue

                required_keys = ("product_id", "name", "price", "quantity")

                if not all(key in item for key in required_keys):
                    print("Missing required fields")
                    continue

                product_id = item["product_id"]

                if product_id <= 0:
                    print("product id must be positive ")
                    continue

                if product_id in self.products:
                    print("Duplicate ID")
                    continue

                price = item["price"]
                
                if isinstance(price, bool) or not isinstance(price, (int, float)):
                    print("Invalid price")
                    continue
                
                if price < 0:
                    print("Negative price")
                    continue
                        
                    
                quantity = item["quantity"]
                 
                if isinstance(quantity, bool) or not isinstance(quantity, (int)):
                    print("Invalid quantity")
                    continue
                        
                if quantity < 0:
                    print("invalid quantity")
                    continue

                name = item["name"]

                if not isinstance(name, str) or not name.strip():
                    print("invalid name ")
                    continue 

                product = Product(
                    product_id,
                    name,
                    price,
                    quantity
                )
                self.products[product.product_id] = product

        except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
            print(f"Could not load inventory file: {error}")

              
def get_positive_integer(prompt): 
    try: 
        value = int(input(prompt))

        if value <= 0:
            print("Please enter a number greater than zero.")
            return None

        return value

    except ValueError:
        print("Please enter a whole number.")
        return None

def get_nonnegative_float(prompt): 
    try: 
        value = float(input(prompt))

        if value < 0:
            print("Price cannot be negative.")
            return None

        return value

    except ValueError:
        print("Please enter a valid number.")
        return None

if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. Add product")
        print("2. Display inventory")
        print("3. Search product")
        print("4. Restock product")
        print("5. Sell product")
        print("6. Remove product")
        print("7. Save inventory")
        print("8. clear file ")
        print("0. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            product_id = get_positive_integer("Product ID: ")
            if product_id is None:
                continue

            name = input("Product name: ").strip()
            if not name:
                print("Product name cannot be empty.")
                continue

            price = get_nonnegative_float("Price: ₹")
            if price is None:
                continue

            quantity = get_positive_integer("Starting quantity: ")
            if quantity is None:
                continue

            product = Product(product_id, name, price, quantity)
            inventory.add_product(product)

        elif choice == "2":
            inventory.display_products()

        elif choice == "3":
            product_id = get_positive_integer("Product ID to search: ")
            if product_id is None:
                continue

            product = inventory.find_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                product.display_info()

        elif choice == "4":
            product_id = get_positive_integer("Product ID to restock: ")
            quantity = get_positive_integer("Quantity to add: ")

            if product_id is not None and quantity is not None:
                inventory.restock_product(product_id, quantity)

        elif choice == "5":
            product_id = get_positive_integer("Product ID to sell: ")
            quantity = get_positive_integer("Quantity to sell: ")

            if product_id is not None and quantity is not None:
                inventory.sell_product(product_id, quantity)

        elif choice == "6":
            product_id = get_positive_integer("Product ID to remove: ")
            if product_id is not None:
                inventory.remove_product(product_id)

        elif choice == "7":
            inventory.save_to_file()
            print("Save requested.")

        elif choice == "8":
            inventory.clear_products()

        elif choice == "0":
            inventory.save_to_file()
            print("Inventory saved. Goodbye!")
            break

        else:
            print("Invalid choice. Select one of the listed options.")

'''For example, in your Inventory Management System, try adding a feature that displays only products whose quantity is below 5.'''