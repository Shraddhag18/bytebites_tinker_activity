# ByteBites Tinker Activity

A campus food ordering app backend designed using object-oriented principles and UML-style class diagrams.

## Overview

This project translates a raw product feature request into a clean system architecture using Python classes. It was built as part of a guided activity exploring AI-assisted design and object-oriented programming.

The workflow covered:
- Identifying core data objects from a feature request
- Designing a UML class diagram with AI collaboration
- Implementing Python class scaffolds from the diagram
- Adding algorithmic methods (filtering, sorting, total calculation)
- Writing and validating a pytest test suite

## System Design

The backend is modeled around four core classes:

| Class | Responsibility |
|---|---|
| `Customer` | Stores name and purchase history; verifies the user is real |
| `MenuItem` | Stores name, price, category, and popularity rating |
| `Menu` | Holds all items; supports filtering by category and sorting |
| `Order` | Groups selected items for a customer and computes total cost |

See [bytebites_spec.md](bytebites_spec.md) for the full feature request, candidate classes, and UML class diagram.

## Files

| File | Description |
|---|---|
| `bytebites_spec.md` | Feature request, candidate classes, and Mermaid UML diagram |
| `draft_from_copilot.md` | Initial AI-generated UML draft with review notes |
| `bytebites_design.md` | Final verified UML class diagram |
| `models.py` | Python class implementations with filtering, sorting, and order logic |
| `test_bytebites.py` | 12 pytest tests covering happy path and edge cases |
| `.github/agents/agent.agent.md` | Custom AI agent scoped to the ByteBites design |

## Running Tests

```bash
python -m pytest test_bytebites.py -v
```

Expected output: **12 passed**
