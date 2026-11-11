"""Basic operations and traversal for Python strings."""

# 1. Length
s = "UTKARSH"
print(len(s))  # 7

# 2. Traverse directly through characters
word = "PYTHON"
for ch in word:
    print(ch)

# 3. Traverse through indexes
for i in range(len(word)):
    print(i, word[i])

# Direct character traversal is convenient when only the character is needed.
# Index-based traversal is useful when the position is also needed.

# 4. Concatenation: joining strings with +
first = "Hello"
second = "World"
combined = first + " " + second
print(combined)  # Hello World

# 5. Repetition
print("Hi" * 3)  # HiHiHi

# 6. Equality and inequality
a = "apple"
b = "apple"
c = "Apple"
print(a == b)  # True
print(a != c)  # True (comparison is case-sensitive)

# 7. Lexicographical comparison
# Python compares strings character by character using Unicode code points.
print("apple" < "banana")  # True
