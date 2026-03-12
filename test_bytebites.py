from models import Customer, MenuItem, Menu, Order


# --- Customer Tests ---

def test_customer_verify_user_with_name():
    # Verify that a customer with a name is considered a real user
    customer = Customer("Alice")
    assert customer.verify_user() is True

def test_customer_verify_user_empty_name():
    # Verify that a customer with an empty name fails verification
    customer = Customer("")
    assert customer.verify_user() is False

def test_customer_purchase_history_starts_empty():
    # A new customer should have no purchase history
    customer = Customer("Alice")
    assert customer.purchase_history == []

def test_customer_add_to_history():
    # Verify that placing an order adds it to purchase history
    customer = Customer("Alice")
    item = MenuItem("Burger", 8.99, "Mains", 4.5)
    order = Order(customer)
    order.add_item(item)
    customer.add_to_history(order)
    assert len(customer.purchase_history) == 1


# --- MenuItem Tests ---

def test_menu_item_stores_attributes():
    # Verify all attributes are stored correctly on a MenuItem
    item = MenuItem("Spicy Burger", 8.99, "Mains", 4.5)
    assert item.name == "Spicy Burger"
    assert item.price == 8.99
    assert item.category == "Mains"
    assert item.popularity_rating == 4.5


# --- Menu Tests ---

def test_filter_by_category_returns_correct_items():
    # Verify that filtering 'Drinks' only returns drink items
    menu = Menu()
    menu.add_item(MenuItem("Soda", 2.49, "Drinks", 3.8))
    menu.add_item(MenuItem("Burger", 8.99, "Mains", 4.5))
    result = menu.filter_by_category("Drinks")
    assert len(result) == 1
    assert result[0].name == "Soda"

def test_filter_by_category_no_match_returns_empty():
    # Verify that filtering a missing category returns an empty list
    menu = Menu()
    menu.add_item(MenuItem("Burger", 8.99, "Mains", 4.5))
    result = menu.filter_by_category("Desserts")
    assert result == []

def test_sort_by_popularity_highest_first():
    # Verify items are sorted by popularity rating from highest to lowest
    menu = Menu()
    menu.add_item(MenuItem("Soda", 2.49, "Drinks", 3.8))
    menu.add_item(MenuItem("Brownie", 3.99, "Desserts", 4.9))
    menu.add_item(MenuItem("Burger", 8.99, "Mains", 4.5))
    result = menu.sort_by_popularity()
    assert result[0].name == "Brownie"
    assert result[-1].name == "Soda"

def test_sort_by_price_lowest_first():
    # Verify items are sorted by price from lowest to highest
    menu = Menu()
    menu.add_item(MenuItem("Burger", 8.99, "Mains", 4.5))
    menu.add_item(MenuItem("Soda", 2.49, "Drinks", 3.8))
    result = menu.sort_by_price()
    assert result[0].name == "Soda"
    assert result[-1].name == "Burger"


# --- Order Tests ---

def test_calculate_total_with_multiple_items():
    # Verify that total is correctly computed for multiple items
    customer = Customer("Alice")
    order = Order(customer)
    order.add_item(MenuItem("Burger", 10.00, "Mains", 4.5))
    order.add_item(MenuItem("Soda", 5.00, "Drinks", 3.8))
    assert order.compute_total() == 15.00

def test_order_total_is_zero_when_empty():
    # Verify that an empty order returns a total of $0
    customer = Customer("Alice")
    order = Order(customer)
    assert order.compute_total() == 0

def test_order_links_to_customer():
    # Verify that the order correctly references the customer
    customer = Customer("Bob")
    order = Order(customer)
    assert order.customer.name == "Bob"
