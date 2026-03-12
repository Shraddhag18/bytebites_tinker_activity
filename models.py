# ByteBites Models
# Four core classes for the ByteBites food ordering app backend.
#
# Customer  - represents a user with a name and purchase history
# MenuItem  - represents a food item with name, price, category, and popularity rating
# Menu      - holds all menu items and supports filtering by category
# Order     - groups selected items into a transaction and computes the total cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def verify_user(self):
        # Returns True if the customer has a non-empty name
        return len(self.name) > 0

    def add_to_history(self, order):
        # Records a completed order in the customer's purchase history
        self.purchase_history.append(order)


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        # Returns all items matching the given category
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        # Returns items sorted by popularity rating, highest first
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)

    def sort_by_price(self):
        # Returns items sorted by price, lowest first
        return sorted(self.items, key=lambda item: item.price)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.selected_items = []

    def add_item(self, item):
        self.selected_items.append(item)

    def compute_total(self):
        # Sums the price of all selected items
        return sum(item.price for item in self.selected_items)


# --- Manual Test Scenario ---
if __name__ == "__main__":
    # Set up customer
    customer = Customer("Alice")
    print(f"Customer: {customer.name} | Verified: {customer.verify_user()}")

    # Set up menu items
    burger = MenuItem("Spicy Burger", 8.99, "Mains", 4.5)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 3.8)
    brownie = MenuItem("Chocolate Brownie", 3.99, "Desserts", 4.9)
    wrap = MenuItem("Veggie Wrap", 6.49, "Mains", 3.2)

    # Build menu
    menu = Menu()
    for item in [burger, soda, brownie, wrap]:
        menu.add_item(item)

    # Filter by category
    print(f"Mains: {[i.name for i in menu.filter_by_category('Mains')]}")

    # Sort by popularity
    print(f"By popularity: {[i.name for i in menu.sort_by_popularity()]}")

    # Sort by price
    print(f"By price: {[i.name for i in menu.sort_by_price()]}")

    # Place an order
    order = Order(customer)
    order.add_item(burger)
    order.add_item(soda)
    print(f"Order total for {order.customer.name}: ${order.compute_total():.2f}")

    # Add to purchase history
    customer.add_to_history(order)
    print(f"Purchase history count: {len(customer.purchase_history)}")
