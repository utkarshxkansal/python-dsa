# Python DSA

A practical, continuously updated record of my **Data Structures and Algorithms journey in Python**. This repository contains my implementations, Jupyter practice notebooks, and problem solutions as I work through core DSA concepts and Striver's learning roadmap.

## Repository map

| Section | What you'll find |
|---|---|
| [Linked Lists](linked_lists/) | Singly, doubly, and circular linked-list operations |
| [Stacks & Queues](stacks_and_queues/) | Stack and queue implementations, including array/list and linked-list approaches |
| [Trees](trees/) | Binary-tree construction, traversals, and problem solutions |
| [Strings](strings/) | String fundamentals, operations, and built-in methods |
| [Striver DSA](striver_dsa/) | Topic-wise practice for basics, hashing, and sorting |

## Current binary-tree practice

- [Tree introduction](trees/binary_trees/introduction.ipynb)
- [Preorder traversal](trees/binary_trees/preorder.ipynb)
- [Inorder traversal](trees/binary_trees/inorder.ipynb)
- [Level-order traversal — LeetCode 102](trees/binary_trees/level_order_traversal.py)
- [All three traversals using one stack](trees/binary_trees/iterative_all_traversals.py)
- [Maximum depth — LeetCode 104](trees/binary_trees/maximum_depth.py)
- [Same tree — LeetCode 100](trees/binary_trees/same_tree.py)

## How this repository is organised

- Topic folders keep related implementations together.
- Jupyter notebooks preserve hands-on experiments and step-by-step learning.
- Standalone `.py` files contain reusable or problem-platform-style solutions.
- Each major topic has its own README with a quick index.
- File names use lowercase `snake_case` for consistency.

## Suggested learning workflow

1. Understand the concept and its invariants.
2. Implement the operation without relying on shortcuts.
3. Trace the code with a small example.
4. Test empty inputs, one-element cases, and boundary conditions.
5. Record time and space complexity.
6. Solve related problems and revisit mistakes.

## Setup

```bash
git clone https://github.com/utkarshxkansal/python-dsa.git
cd python-dsa
python -m pip install jupyter
jupyter notebook
```

Open any `.ipynb` notebook in Jupyter Notebook, JupyterLab, or VS Code. Standalone Python files can be run with:

```bash
python path/to/file.py
```

## Progress roadmap

- [x] Linked-list fundamentals and operations
- [x] Stack and queue implementation practice
- [x] Binary-tree fundamentals and traversal practice
- [x] String fundamentals and common operations
- [x] Striver basics, hashing, and sorting practice
- [ ] Balanced binary tree and further binary-tree problems
- [ ] Recursion and backtracking
- [ ] Binary search, heaps, graphs, and dynamic programming

*This is a learning repository: coverage grows as concepts are studied, implemented, tested, and documented.*
