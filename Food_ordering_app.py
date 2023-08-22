#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class Restaurant:
    def __init__(self):
        self.food_items = {}
        self.users = {}
        self.current_user = None

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add new food item")
            print("2. Edit food item")
            print("3. View food item list")
            print("4. Remove food item")
            print("0. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_food_item()
            elif choice == 2:
                self.edit_food_item()
            elif choice == 3:
                self.view_food_items()
            elif choice == 4:
                self.remove_food_item()
            elif choice == 0:
                break
            else:
                print("Invalid choice!")

    def user_menu(self):
        while True:
            print("\nUser Menu:")
            print("1. Place New Order")
            print("2. Order History")
            print("3. Update Profile")
            print("0. Logout")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.place_new_order()
            elif choice == 2:
                self.view_order_history()
            elif choice == 3:
                self.update_profile()
            elif choice == 0:
                self.current_user = None
                break
            else:
                print("Invalid choice!")

    def add_food_item(self):
        name = input("Enter food item name: ")
        quantity = input("Enter quantity: ")
        price = float(input("Enter price: "))
        discount = float(input("Enter discount: "))
        stock = int(input("Enter stock: "))
        food_id = len(self.food_items) + 1
        self.food_items[food_id] = FoodItem(name, quantity, price, discount, stock)
        print("Food item added successfully!")

    def edit_food_item(self):
        food_id = int(input("Enter FoodID of the item to edit: "))
        if food_id in self.food_items:
            food_item = self.food_items[food_id]
            print("Current Details:")
            print("Name:", food_item.name)
            print("Quantity:", food_item.quantity)
            print("Price:", food_item.price)
            print("Discount:", food_item.discount)
            print("Stock:", food_item.stock)
            food_item.name = input("Enter new name: ")
            food_item.quantity = input("Enter new quantity: ")
            food_item.price = float(input("Enter new price: "))
            food_item.discount = float(input("Enter new discount: "))
            food_item.stock = int(input("Enter new stock: "))
            print("Food item edited successfully!")
        else:
            print("Food item not found!")

    def view_food_items(self):
        print("\nFood Item List:")
        for food_id, food_item in self.food_items.items():
            print(f"FoodID: {food_id}")
            print("Name:", food_item.name)
            print("Quantity:", food_item.quantity)
            print("Price:", food_item.price)
            print("Discount:", food_item.discount)
            print("Stock:", food_item.stock)
            print("-" * 30)

    def remove_food_item(self):
        food_id = int(input("Enter FoodID of the item to remove: "))
        if food_id in self.food_items:
            del self.food_items[food_id]
            print("Food item removed successfully!")
        else:
            print("Food item not found!")

    def place_new_order(self):
        print("\nAvailable Food Items:")
        for food_id, food_item in self.food_items.items():
            print(f"{food_id}. {food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

        selected_items = input("Enter the array of numbers for selected items (e.g., 2 3): ").split()
        selected_item_ids = [int(item_id) for item_id in selected_items]
        
        order_items = []
        total_amount = 0
        for item_id in selected_item_ids:
            if item_id in self.food_items:
                order_items.append(self.food_items[item_id])
                total_amount += self.food_items[item_id].price

        print("\nSelected Items:")
        for item in order_items:
            print(f"{item.name} ({item.quantity}) [INR {item.price}]")

        place_order = input("Do you want to place the order? (yes/no): ")
        if place_order.lower() == "yes":
            for item in order_items:
                item.stock -= 1
            self.current_user.orders.append(order_items)
            print("Order placed successfully!")

    def view_order_history(self):
        print("\nOrder History:")
        for idx, order_items in enumerate(self.current_user.orders, start=1):
            print(f"Order {idx}:")
            for item in order_items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            print("-" * 30)

    def update_profile(self):
        print("\nUpdate Profile:")
        self.current_user.full_name = input("Enter new full name: ")
        self.current_user.phone_number = input("Enter new phone number: ")
        self.current_user.email = input("Enter new email: ")
        self.current_user.address = input("Enter new address: ")
        self.current_user.password = input("Enter new password: ")
        print("Profile updated successfully!")

    def run(self):
        while True:
            print("\nWelcome to the Restaurant App!")
            print("1. Admin Login")
            print("2. User Login")
            print("0. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                admin_username = input("Enter admin username: ")
                admin_password = input("Enter admin password: ")
                if admin_username == "admin" and admin_password == "admin":
                    self.admin_menu()
                else:
                    print("Invalid admin credentials!")
            elif choice == 2:
                email = input("Enter email: ")
                password = input("Enter password: ")
                if email in self.users and self.users[email].password == password:
                    self.current_user = self.users[email]
                    self.user_menu()
                else:
                    print("Invalid user credentials!")
            elif choice == 0:
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    restaurant_app = Restaurant()
    restaurant_app.run()

