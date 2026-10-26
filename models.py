# ByteBites Models
# Customer: Stores a customer's name and purchase history.
# MenuItem: Stores an item's name, price, category, and popularity.
# Menu: Stores menu items and supports filtering and sorting.
# Order: Stores selected items and calculates their total cost.


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        self.purchase_history.append(order)


class MenuItem:
    def __init__(self, name, price, category, popularity):
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, MenuItem):
            raise TypeError("Only MenuItem objects can be added.")
        self.items.append(item)

    def filter_by_category(self, category):
        return [
            item for item in self.items
            if item.category.lower() == category.lower()
        ]

    def sort_by_popularity(self):
        return sorted(
            self.items,
            key=lambda item: item.popularity,
            reverse=True
        )


class Order:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

        if not all(isinstance(item, MenuItem) for item in self.items):
            raise TypeError("All order entries must be MenuItem objects.")

    def calculate_total(self):
        return sum(item.price for item in self.items)
