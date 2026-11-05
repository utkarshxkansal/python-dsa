"""String fundamentals: creation, indexing, slicing, and immutability."""

# 1. Creating strings
name = "UTKARSH"
message = 'Learning Python strings'

print(name)
print(message)

# 2. Positive indexing (starts at 0)
s = "PYTHON"
print(s[0])  # P
print(s[1])  # Y
print(s[4])  # O

# 3. Negative indexing (counts from the end)
print(s[-1])  # N
print(s[-2])  # O
print(s[-3])  # H

# 4. Slicing: string[start:end:step]
# The end index is excluded.
print(s[0:3])  # PYT
print(s[2:5])  # THO
print(s[:3])   # PYT (start defaults to 0)
print(s[3:])   # HON (end defaults to len(s))
print(s[::-1]) # NOHTYP (traverse backwards)

# 5. Strings are immutable: this raises TypeError.
# s[0] = "J"

# To create a changed string, build a new one.
original = "HELLO"
changed = "Y" + original[1:]
print(original)  # HELLO: original is unchanged
print(changed)   # YELLO

# 6. Useful boundary examples
empty = ""
print(len(empty))  # 0
print(s[0:0])       # empty string
