
classDiagram
    class Customer {
        +str name
        +list purchase_history
        +__init__(name)
        +add_purchase(order)
    }

    class MenuItem {
        +str name
        +float price
        +str category
        +float popularity
        +__init__(name, price, category, popularity)
    }

    class Menu {
        +list items
        +__init__()
        +add_item(item)
        +filter_by_category(category)
        +sort_by_popularity()
    }

    class Order {
        +list items
        +__init__(items)
        +calculate_total()
    }

    Menu "1" o-- "*" MenuItem : contains
    Order "1" o-- "*" MenuItem : selects
    Customer "1" --> "*" Order : purchase history
