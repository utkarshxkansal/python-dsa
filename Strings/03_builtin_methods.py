"""Common built-in string methods useful in Python and DSA."""

# Most string methods return a new string; they do not mutate the original.

# 1. Case conversion
s = "UtKaRsH"
print(s.lower())  # utkarsh
print(s.upper())  # UTKARSH
print(s)          # UtKaRsH (unchanged)

# Case-insensitive comparison
left = "Madam"
right = "madam"
print(left.lower() == right.lower())  # True

# 2. Removing surrounding whitespace
text = "   hello world   "
print(text.strip())   # "hello world"
print(text.lstrip())  # removes whitespace on the left
print(text.rstrip())  # removes whitespace on the right
# strip() does not remove whitespace from the middle.

# 3. Replacing substrings
language = "I love Java"
print(language.replace("Java", "Python"))  # I love Python
print("banana".replace("a", "x", 2))      # bxnxna (at most 2 replacements)

# 4. Splitting a string into a list
sentence = "I love Python"
print(sentence.split())  # ['I', 'love', 'Python']

csv_text = "apple,banana,mango"
print(csv_text.split(","))  # ['apple', 'banana', 'mango']

print("A-B-C-D".split("-", 1))  # ['A', 'B-C-D']

# 5. Counting non-overlapping occurrences
fruit = "banana"
print(fruit.count("a"))    # 3
print(fruit.count("n"))    # 2
print(fruit.count("z"))    # 0
print("banana".count("ana"))  # 1 (non-overlapping count)

# 6. Finding a substring
word = "programming"
print(word.find("g"))    # 3: first matching index
print(word.find("ram"))  # 3
print(word.find("xyz"))  # -1: not found

# index() also finds a substring, but raises ValueError if it is absent.
print("python".index("t"))  # 2
# "python".index("z")       # ValueError

# 7. Prefix and suffix checks
filename = "notes.py"
print(filename.startswith("notes"))  # True
print(filename.endswith(".py"))      # True

# 8. Character/string validation methods
print("Hello".isalpha())   # True: letters only
print("123".isdigit())     # True: digits only
print("abc123".isalnum())  # True: letters or digits
print("   ".isspace())     # True: whitespace only

# 9. Other useful formatting methods
print("hello".capitalize())    # Hello
print("hello world".title())   # Hello World
print("HeLLo".swapcase())      # hEllO

# DSA reminder:
# Built-in methods are useful, but practise implementing core logic yourself.
# For example, later we will count character frequencies using a dictionary.
