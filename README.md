# ByteBites Tinker Activity

A campus food ordering app backend designed using object-oriented principles and UML-style class diagrams.

## Overview

This project translates a raw product feature request into a clean system architecture using Python classes. It was built as part of a guided activity exploring AI-assisted design and object-oriented programming.

## System Design

The backend is modeled around four core classes:

| Class | Responsibility |
|---|---|
| `Customer` | Stores name and purchase history |
| `MenuItem` | Stores name, price, category, and popularity rating |
| `Menu` | Holds all items and supports filtering by category |
| `Order` | Groups selected items and computes total cost |

See [bytebites_spec.md](bytebites_spec.md) for the full feature request, candidate classes, and UML class diagram.

## Files

- `bytebites_spec.md` — Feature spec, candidate classes, and Mermaid UML diagram
- `draft_from_copilot.md` — AI-generated UML draft with review notes
- `.github/agents/agent.agent.md` — Custom AI agent for generating ByteBites UML and scaffolds
