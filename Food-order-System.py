class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

def main():
    menu = {
        "Pizza": 10,
        "Burger": 5,
        "Pasta": 8,
        "Salad": 6
    }

    print("Welcome to the Food Ordering System!")
    print("Here is our menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    order = Order()
    while True:
        choice = input("Enter the item you want to order (or 'done' to finish): ")
        if choice == "done":
            break
        elif choice in menu:
            item = FoodItem(choice, menu[choice])
            order.add_item(item)
            print(f"{choice} added to your order.")
        else:
            print("Invalid choice. Please select from the menu.")

    print("Your order:")
    for item in order.items:
        print(f"{item.name}: ${item.price}")
    print(f"Total price: ${order.total_price()}")

main()
