# Draft UML Class Diagram

Generated from `bytebites_spec.md` candidate classes.

```mermaid
classDiagram
    class Customer {
        +String name
        +List~Order~ purchaseHistory
        +verifyUser() bool
    }

    class MenuItem {
        +String name
        +float price
        +String category
        +float popularityRating
    }

    class Menu {
        +List~MenuItem~ items
        +filterByCategory(category: String) List~MenuItem~
        +addItem(item: MenuItem) void
    }

    class Order {
        +List~MenuItem~ selectedItems
        +Customer customer
        +computeTotal() float
    }

    Customer "1" --> "0..*" Order : places
    Order "1" --> "1..*" MenuItem : contains
    Menu "1" --> "0..*" MenuItem : holds
```

## Review Notes

- All 4 classes match the candidate list (Customer, MenuItem, Menu, Order)
- Attributes align with the feature request descriptions
- No unexpected classes added
- Relationships are consistent with the spec
