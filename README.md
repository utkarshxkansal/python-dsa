# Python DSA — Learning & Implementation

A hands-on record of my journey through **Data Structures and Algorithms using Python**. This repository contains implementations, practice work, and notes created while learning how data structures behave internally—not just how to use built-in shortcuts.

> Current focus: understanding each structure, implementing its core operations, testing edge cases, and gradually solving problems with it.

## Topics

| Topic | Current coverage |
|---|---|
| Linked Lists | Singly, doubly, and circular linked lists |
| Stacks | Array/list-based implementations and related problems |
| Queues | Linear queue, fixed-capacity array queue, and upcoming variants |
| Trees | Binary tree fundamentals and traversals |

This table describes the learning areas in the repository; individual implementations may still be in progress.

## Repository layout

```text
python-dsa/
├── Linked_List/
│   ├── Doubly_ll/
│   ├── Singly_Linked_List/
│   └── circular_ll/
├── Stack Queue/
│   ├── Queue/
│   └── Stack/
├── Trees/
│   └── Binary Trees/
├── .gitignore
└── README.md
```

Folder names are kept as they currently exist so existing notebook and file paths are not broken. They can be renamed in a dedicated cleanup when all references are updated together.

## How I study each topic

1. Understand the purpose and invariants of the data structure.
2. Implement the structure and its operations from scratch.
3. Trace pointer/index changes with small examples.
4. Test normal cases, empty structures, boundary conditions, and invalid operations.
5. Analyse time and space complexity.
6. Practise problems that use the structure.

## Implementation checklist

For each data structure, aim to document:

- [ ] Core operations and their behaviour
- [ ] Edge cases (empty, one element, and boundary conditions)
- [ ] Time and space complexity
- [ ] Example usage and expected output
- [ ] Problems solved using the concept

## Learning roadmap

- [x] Singly, doubly, and circular linked-list practice
- [x] Begin stack implementations
- [x] Begin queue implementations
- [x] Begin binary-tree practice
- [ ] Complete array-based and linked-list-based stack/queue variants
- [ ] Circular queue and deque
- [ ] Recursion and backtracking
- [ ] Searching and sorting
- [ ] Heaps, hash tables, graphs, and dynamic programming
- [ ] Add problem explanations and complexity notes as topics mature

## Tools

- Python
- Jupyter Notebook
- Git and GitHub

## Running the notebooks

1. Clone this repository.
2. Install Python and Jupyter Notebook.
3. Open the relevant `.ipynb` file in Jupyter or VS Code.
4. Run cells in order and check the examples yourself.

## Repository principles

- Prefer clear, understandable implementations over clever one-liners.
- Keep experiments and unfinished work clearly labelled.
- Explain non-obvious logic and important edge cases.
- Never commit credentials, private data, or local environment folders.

---

*Learning by implementing, debugging, testing, and improving—one concept at a time.*
