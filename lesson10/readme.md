# Lesson 10: Working with Strings

[Back to the main roadmap](../README.md) | [Previous lesson: Dictionaries](../lesson9/readme.md)

## What is a String?

A **string** is a sequence of characters enclosed in quotes.

Examples:

```python
name = "Alex"
city = 'Delhi'
```

You can use either **single quotes (`'`)** or **double quotes (`"`). Both work the same way.

---

# Strings are Indexed

Just like lists, every character in a string has an index.

Indexes start at **0**.

### Example

```python
word = "Python"

print(word[0])
print(word[1])
print(word[-1])
```

### Output

```text
P
y
n
```

Negative indexes count from the end.

- `-1` → Last character
- `-2` → Second last character

---

# String Slicing

You can extract part of a string using slicing.

### Example

```python
word = "Python"

print(word[0:3])
print(word[2:])
print(word[:2])
print(word[::-1])
```

### Output

```text
Pyt
thon
Py
nohtyP
```

### Slice Syntax

```text
string[start:stop:step]
```

- `start` → Beginning index
- `stop` → Ending index (not included)
- `step` → How many positions to move each time

The expression:

```python
word[::-1]
```

is a common Python trick to reverse a string.

---

# Strings are Immutable

Strings **cannot be modified** after they are created.

### Example

```python
word = "Python"

word[0] = "J"
```

### Output

```text
TypeError: 'str' object does not support item assignment
```

Instead, create a new string.

```python
word = "Python"

word = "J" + word[1:]

print(word)
```

### Output

```text
Jython
```

---

# Finding the Length

Use `len()` to count the number of characters.

### Example

```python
name = "Alex"

print(len(name))
```

### Output

```text
4
```

---

# Concatenation

Concatenation means joining strings together.

### Example

```python
first = "Alex"
last = "Kumar"

full_name = first + " " + last

print(full_name)
```

### Output

```text
Alex Kumar
```

---

## Mixing Strings and Numbers

This causes an error.

```python
age = 10

print("Age: " + age)
```

### Output

```text
TypeError
```

Convert the number to a string.

```python
print("Age: " + str(age))
```

### Output

```text
Age: 10
```

---

# f-Strings (Recommended)

The easiest way to combine variables with text.

### Example

```python
name = "Alex"
age = 10

print(f"My name is {name} and I am {age} years old.")
```

### Output

```text
My name is Alex and I am 10 years old.
```

You can even perform calculations inside `{}`.

```python
price = 19.99

print(f"Total with tax: {price * 1.08:.2f}")
```

### Output

```text
Total with tax: 21.59
```

`:.2f` means display exactly **2 decimal places**.

---

# Common String Methods

```python
text = "  Hello World  "
```

| Method | Description |
|---------|-------------|
| `strip()` | Remove spaces from both ends |
| `lower()` | Convert to lowercase |
| `upper()` | Convert to uppercase |
| `title()` | Capitalize every word |
| `replace(old, new)` | Replace text |

### Example

```python
text = "  Hello World  "

print(text.strip())
print(text.lower())
print(text.upper())
print(text.title())
print(text.replace("World", "Python"))
```

### Output

```text
Hello World
  hello world
  HELLO WORLD
  Hello World
  Hello Python
```

Remember:

String methods **do not change the original string**.

If you want the change to stay:

```python
text = text.strip()
```

---

# Splitting Strings

`split()` converts a string into a list.

### Example

```python
sentence = "the quick brown fox"

words = sentence.split()

print(words)
```

### Output

```text
['the', 'quick', 'brown', 'fox']
```

---

## Splitting Using a Specific Character

```python
csv = "apple,banana,cherry"

items = csv.split(",")

print(items)
```

### Output

```text
['apple', 'banana', 'cherry']
```

---

# Joining Strings

`join()` combines a list into a string.

### Example

```python
words = ["the", "quick", "brown", "fox"]

sentence = " ".join(words)

print(sentence)
```

### Output

```text
the quick brown fox
```

---

# Searching in Strings

### Example

```python
text = "Hello World"

print("World" in text)
print(text.startswith("Hello"))
print(text.endswith("World"))
print(text.find("World"))
print(text.count("l"))
```

### Output

```text
True
True
True
6
3
```

| Method | Description |
|---------|-------------|
| `in` | Check if text exists |
| `startswith()` | Starts with text |
| `endswith()` | Ends with text |
| `find()` | Returns index or `-1` |
| `count()` | Counts occurrences |

---

# Character Validation

These methods help validate user input.

### Example

```python
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print("   ".isspace())
```

### Output

```text
True
True
True
True
```

| Method | Checks |
|---------|--------|
| `isdigit()` | Digits only |
| `isalpha()` | Letters only |
| `isalnum()` | Letters and numbers |
| `isspace()` | Whitespace only |

---

# String Multiplication

Strings can be repeated using `*`.

### Example

```python
print("ha" * 3)

print("-" * 20)
```

### Output

```text
hahaha
--------------------
```

This is useful for separators.

---

# Real-World Example

```python
raw_input = "  Alex Kumar, 25, Chennai  "

cleaned = raw_input.strip()

parts = cleaned.split(",")

name = parts[0].strip()
age = parts[1].strip()
city = parts[2].strip()

print(f"Name: {name}, Age: {age}, City: {city}")
```

### Output

```text
Name: Alex Kumar, Age: 25, City: Chennai
```

This pattern is very common when working with:

- User input
- CSV files
- APIs
- Forms

---

# Practice Program

Create a file named **`lesson_strings.py`**.

```python
name = "  Python Programming  "

# 1. Clean it up
clean_name = name.strip()
print(f"'{clean_name}'")

# 2. Case methods
print(clean_name.upper())
print(clean_name.lower())

# 3. Slicing
print(clean_name[0:6])
print(clean_name[::-1])

# 4. f-strings with logic
age = 10
years_until_18 = 18 - age

print(f"You have {years_until_18} years until you're 18")

# 5. Split and join
sentence = "I love learning Python"

words = sentence.split()

print(words)
print(len(words))

reversed_sentence = " ".join(words[::-1])

print(reversed_sentence)

# 6. Searching
review = "This course is amazing and well explained"

print("amazing" in review)
print(review.find("well"))
print(review.count("a"))

# 7. Validation
user_input = "12a5"

if user_input.isdigit():
    print("Valid number:", int(user_input))
else:
    print("Invalid number entered")
```

### Sample Output

```text
'Python Programming'
PYTHON PROGRAMMING
python programming
Python
gnimmargorP nohtyP
You have 8 years until you're 18

['I', 'love', 'learning', 'Python']
4
Python learning love I

True
27
5

Invalid number entered
```

---

# Key Takeaways

- Strings are sequences of characters.
- Strings support indexing and slicing.
- Strings are **immutable** (cannot be modified directly).
- Use `len()` to get the length.
- Use `+` to concatenate strings.
- Prefer **f-strings** for formatting text.
- String methods return new strings.
- `split()` converts a string into a list.
- `join()` converts a list into a string.
- Use methods like `find()`, `count()`, and `startswith()` to search strings.
- Use `isdigit()`, `isalpha()`, and related methods to validate input.
- Strings can be repeated using the `*` operator.

---

**Next Lesson:** Data Structures & Algorithms – Arrays and Linked Lists