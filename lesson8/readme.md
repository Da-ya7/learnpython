# Lesson 8: Lists, Tuples, and Sets

[Back to the main roadmap](../README.md) | [Previous lesson: Loops](../lesson7/readme.md)

## What are Collections?

Sometimes you need to store **multiple values** in a single variable.

Python provides several collection types for this:

- **List** → Ordered and changeable
- **Tuple** → Ordered but unchangeable
- **Set** → Unordered with unique values

The biggest differences are:

- Can you change it?
- Does order matter?
- Are duplicate values allowed?

---

# 1. Lists

## What is a List?

A **list** is an **ordered** and **changeable** collection.

Think of it like a shopping list written in pencil—you can add, remove, or change items whenever you want.

### Example

```python
fruits = ["apple", "banana", "cherry"]

print(fruits)
```

### Output

```text
['apple', 'banana', 'cherry']
```

Lists use **square brackets `[]`**.

---

# Accessing Items (Indexing)

Each item has an index.

Indexes start at **0**, not **1**.

### Example

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

### Output

```text
apple
banana
cherry
```

---

# Negative Indexing

Negative indexes count from the end.

### Example

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[-1])
print(fruits[-2])
```

### Output

```text
cherry
banana
```

Remember:

- `-1` → Last item
- `-2` → Second last
- `-3` → Third last

---

# List Slicing

Slicing extracts part of a list.

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])
print(numbers[:2])
print(numbers[2:])
print(numbers[:])
```

### Output

```text
[20, 30]
[10, 20]
[30, 40, 50]
[10, 20, 30, 40, 50]
```

### Rule

```text
list[start:stop]
```

- Includes `start`
- Stops before `stop`

---

# Modifying a List

Lists are mutable, meaning they can be changed.

### Example

```python
fruits = ["apple", "banana", "cherry"]

fruits[0] = "mango"

print(fruits)
```

### Output

```text
['mango', 'banana', 'cherry']
```

---

# Common List Methods

```python
fruits = ["apple", "banana"]

fruits.append("cherry")
fruits.insert(1, "kiwi")
fruits.remove("banana")
fruits.pop()
fruits.pop(0)
fruits.sort()
fruits.reverse()

print(len(fruits))
print("kiwi" in fruits)

fruits.clear()
```

| Method | Description |
|---------|-------------|
| `append()` | Add item to the end |
| `insert()` | Insert item at a specific position |
| `remove()` | Remove by value |
| `pop()` | Remove by index (default: last) |
| `sort()` | Sort the list |
| `reverse()` | Reverse the list |
| `len()` | Count items |
| `in` | Check membership |
| `clear()` | Remove all items |

---

# Copying a List

This is a very common beginner mistake.

### Incorrect

```python
list_a = [1, 2, 3]

list_b = list_a

list_b.append(4)

print(list_a)
```

### Output

```text
[1, 2, 3, 4]
```

Both variables point to the same list.

---

### Correct

```python
list_a = [1, 2, 3]

list_b = list_a.copy()

list_b.append(4)

print(list_a)
print(list_b)
```

### Output

```text
[1, 2, 3]
[1, 2, 3, 4]
```

Use `.copy()` when you need an independent copy.

---

# List Comprehension

A shorter way to create lists.

### Example

```python
squares = [x * x for x in range(5)]

print(squares)
```

### Output

```text
[0, 1, 4, 9, 16]
```

You'll learn list comprehensions in more detail later.

---

# 2. Tuples

## What is a Tuple?

A tuple is an **ordered** but **immutable** collection.

Once created, it cannot be changed.

### Example

```python
point = (10, 20)

print(point[0])
print(point[1])
```

### Output

```text
10
20
```

Tuples use **parentheses `()`**.

---

# Why Use Tuples?

Tuples are useful when data should never change.

Examples:

- GPS coordinates
- RGB color values
- Days of the week

### Example

```python
color = (255, 0, 0)
```

---

# Trying to Modify a Tuple

```python
point = (10, 20)

point[0] = 99
```

### Output

```text
TypeError: 'tuple' object does not support item assignment
```

Tuples cannot be modified.

---

# What You Can Do with Tuples

```python
point = (10, 20, 30)

print(len(point))
print(point[1:])
print(20 in point)

for value in point:
    print(value)
```

### Output

```text
3
(20, 30)
True
10
20
30
```

---

# Tuple Unpacking

A tuple can be unpacked into variables.

### Example

```python
point = (10, 20)

x, y = point

print(x)
print(y)
```

### Output

```text
10
20
```

---

# Returning Multiple Values

Functions often return tuples.

### Example

```python
def get_dimensions():
    return (1920, 1080)

width, height = get_dimensions()

print(width)
print(height)
```

### Output

```text
1920
1080
```

---

# One-Item Tuple

A comma creates a tuple.

### Example

```python
not_a_tuple = (5)

actual_tuple = (5,)

print(type(not_a_tuple))
print(type(actual_tuple))
```

### Output

```text
<class 'int'>
<class 'tuple'>
```

---

# 3. Sets

## What is a Set?

A set is an **unordered collection of unique values**.

Duplicate values are removed automatically.

### Example

```python
numbers = {1, 2, 3, 2, 1}

print(numbers)
```

### Output

```text
{1, 2, 3}
```

Sets use **curly braces `{}`**.

**Note:** An empty set is created using:

```python
set()
```

---

# Removing Duplicates

Sets make removing duplicates easy.

### Example

```python
names = ["Alex", "Sam", "Alex", "Jo", "Sam"]

unique_names = set(names)

print(unique_names)
```

### Output

```text
{'Alex', 'Sam', 'Jo'}
```

---

# Fast Membership Testing

Checking membership in a set is very efficient.

### Example

```python
allowed_users = {"Alex", "Sam", "Jo"}

print("Alex" in allowed_users)
```

### Output

```text
True
```

---

# Sets Have No Index

Sets are unordered.

### Example

```python
numbers = {1, 2, 3}

print(numbers[0])
```

### Output

```text
TypeError
```

You cannot access items by index.

---

# Common Set Methods

```python
a = {1, 2, 3}

a.add(4)

a.remove(2)

a.discard(99)
```

| Method | Description |
|---------|-------------|
| `add()` | Add an item |
| `remove()` | Remove an item (error if missing) |
| `discard()` | Remove if present (no error if missing) |

---

# Set Operations

### Example

```python
a = {1, 2, 3, 4}

b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
```

### Output

```text
{1, 2, 3, 4, 5, 6}
{3, 4}
{1, 2}
{1, 2, 5, 6}
```

| Operator | Meaning |
|----------|---------|
| `|` | Union (all items) |
| `&` | Intersection (common items) |
| `-` | Difference |
| `^` | Symmetric Difference |

---

# Quick Comparison

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Ordered | ✅ Yes | ✅ Yes | ❌ No |
| Changeable | ✅ Yes | ❌ No | ✅ Yes |
| Duplicate Values | ✅ Allowed | ✅ Allowed | ❌ Not Allowed |
| Brackets | `[]` | `()` | `{}` |

---

# Practice Program

Create a file named **`lesson_collections.py`**.

```python
# LISTS
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")
fruits.insert(1, "kiwi")

print(fruits)
print(fruits[-1])
print(fruits[1:3])

list_a = [1, 2, 3]
list_b = list_a.copy()

list_b.append(4)

print("list_a:", list_a)
print("list_b:", list_b)


# TUPLES
point = (5, 10)

x, y = point

print(f"x is {x}, y is {y}")


def get_min_max(numbers):
    return (min(numbers), max(numbers))


low, high = get_min_max([4, 7, 1, 9, 2])

print("low:", low, "high:", high)


# SETS
names = ["Alex", "Sam", "Alex", "Jo", "Sam", "Alex"]

unique_names = set(names)

print(unique_names)

math_club = {"Alex", "Sam", "Jo"}
art_club = {"Jo", "Priya", "Sam"}

print("Both clubs:", math_club & art_club)
print("Either club:", math_club | art_club)
print("Math only:", math_club - art_club)
```

### Sample Output

```text
['apple', 'kiwi', 'banana', 'cherry', 'mango']
mango
['kiwi', 'banana']
list_a: [1, 2, 3]
list_b: [1, 2, 3, 4]

x is 5, y is 10
low: 1 high: 9

{'Alex', 'Sam', 'Jo'}
Both clubs: {'Jo', 'Sam'}
Either club: {'Alex', 'Sam', 'Jo', 'Priya'}
Math only: {'Alex'}
```

---

# Key Takeaways

- Lists are ordered, changeable collections.
- Tuples are ordered but immutable.
- Sets store unique values and remove duplicates automatically.
- Lists support indexing, slicing, and many useful methods.
- Tuples support indexing and unpacking but cannot be modified.
- Sets do not support indexing because they are unordered.
- Use `.copy()` to create an independent copy of a list.
- Sets are excellent for removing duplicates and performing set operations like union and intersection.

---

**Next Lesson:** Dictionaries