# Strings in Python — Fundamentals

This folder records the string concepts covered while learning DSA with Python.

## Learning progress

- [x] String creation and character sequences
- [x] Positive and negative indexing
- [x] Slicing and reverse slicing
- [x] String immutability
- [x] Length with `len()`
- [x] Traversal using characters and indexes
- [x] Concatenation and repetition
- [x] String comparison
- [x] Common built-in string methods

## Files

| File | Coverage |
|---|---|
| `01_string_fundamentals.py` | Creation, indexing, slicing, immutability |
| `02_string_operations.py` | Length, traversal, concatenation, repetition, comparison |
| `03_builtin_methods.py` | Case conversion, trimming, replacement, splitting, searching, validation |

## Important Python behaviour

- String indexes start at `0`.
- Negative indexes count from the end; `s[-1]` is the last character.
- In a slice `s[start:end:step]`, the end index is excluded.
- A negative slice step can traverse a string backwards: `s[::-1]`.
- Python strings are immutable. Methods such as `upper()` and `replace()` return new strings rather than modifying the original.
- `find()` returns `-1` when a substring is absent; `index()` raises `ValueError`.
- `count()` counts non-overlapping occurrences.

## How to practise

Run each Python file, predict outputs before executing, and change the examples to test edge cases. The next topics will be character encoding (`ord()` / `chr()`), frequency counting, and common DSA patterns.
