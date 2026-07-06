# Library Management System

A terminal-based library system built as a capstone project for an OOP fundamentals curriculum. No frameworks, no external libraries — just pure Python classes.

---

## OOP Concepts Used

| Concept | Where |
|---|---|
| Encapsulation | `Member` enforces a 3-book borrow limit via `__borrowed` |
| Inheritance | `PhysicalBook` and `EBook` both inherit from `Book` |
| Polymorphism | `Library.borrow_book()` calls `book.borrow()` without knowing the subclass |
| Operator Overloading | `__str__` on `Book` for clean printing |
| Aggregation | `Library` holds books and members it didn't create |
| Abstraction | `Book.borrow()` defines the contract; subclasses implement it |

---

## Project Structure

```
oops-python/
├── library_system.py      ← this project
├── oops_python.ipynb      ← all concept code
├── notes/
│   └── README.md          ← full concept notes + 30 interview questions
├── pdfs/
│   ├── oops_python_notes.pdf
│   └── missed_concepts.pdf
└── class_diagram.svg
```

---

## How to Run

```bash
python library_system.py
```

---

## Learning Context

This project is the final exercise of a structured OOP curriculum covering:

1. Why OOP exists
2. Class and Object
3. Constructor and `self`
4. Encapsulation
5. Static Variables and Methods
6. Collection of Objects
7. Aggregation and Composition
8. Inheritance, MRO, and Polymorphism

Full notes and 30 interview questions are in `notes/README.md`.