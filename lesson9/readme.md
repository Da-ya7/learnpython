# Lesson 9: Dictionaries

[Back to the main roadmap](../README.md) | [Previous lesson: Lists, Tuples, and Sets](../lesson8/readme.md)

## What is a Dictionary?

A **dictionary** stores data as **key-value pairs**.

Unlike lists, where you access items by their position (index), dictionaries let you access values using a **key**.

---

## Real-Life Example

Think of a real dictionary.

You don't search every page until you find a word.

Instead:

- You look up the **word** (key).
- The dictionary gives you the **definition** (value).

Python dictionaries work the same way.

---

# Creating a Dictionary

### Example

```python
person = {
    "name": "Alex",
    "age": 10,
    "city": "Delhi"
}

print(person)
```

### Output

```text
{'name': 'Alex', 'age': 10, 'city': 'Delhi'}
```

Dictionaries use **curly braces `{}`**.

Each item is stored as:

```text
key : value
```

---

# Accessing Values

Use the key to retrieve a value.

### Example

```python
person = {
    "name": "Alex",
    "age": 10
}

print(person["name"])
print(person["age"])
```

### Output

```text
Alex
10
```

Unlike lists, dictionaries do **not** use indexes.

---

# Accessing a Missing Key

If the key doesn't exist, Python raises a `KeyError`.

### Example

```python
person = {
    "name": "Alex"
}

print(person["height"])
```

### Output

```text
KeyError: 'height'
```

---

# Using `.get()`

`.get()` safely retrieves a value.

If the key doesn't exist, it returns `None` or a default value.

### Example

```python
person = {
    "name": "Alex"
}

print(person.get("height"))
print(person.get("height", "Unknown"))
```

### Output

```text
None
Unknown
```

Whenever you're unsure whether a key exists, use `.get()`.

---

# Adding and Updating Values

The same syntax is used for both adding and updating.

### Example

```python
person = {
    "name": "Alex",
    "age": 10
}

person["age"] = 11
person["city"] = "Delhi"

print(person)
```

### Output

```text
{'name': 'Alex', 'age': 11, 'city': 'Delhi'}
```

If the key exists, Python updates it.

If it doesn't exist, Python creates it.

---

# Removing Items

### Using `del`

```python
person = {
    "name": "Alex",
    "age": 10,
    "city": "Delhi"
}

del person["city"]

print(person)
```

### Output

```text
{'name': 'Alex', 'age': 10}
```

---

### Using `.pop()`

`.pop()` removes the key and returns its value.

```python
person = {
    "name": "Alex",
    "age": 10
}

age = person.pop("age")

print(age)
print(person)
```

### Output

```text
10
{'name': 'Alex'}
```

---

# Checking if a Key Exists

The `in` operator checks **keys**, not values.

### Example

```python
person = {
    "name": "Alex",
    "age": 10
}

print("name" in person)
print("Alex" in person)
```

### Output

```text
True
False
```

If you want to check values instead:

```python
print("Alex" in person.values())
```

### Output

```text
True
```

---

# Looping Through a Dictionary

## Loop Through Keys

```python
person = {
    "name": "Alex",
    "age": 10,
    "city": "Delhi"
}

for key in person:
    print(key)
```

### Output

```text
name
age
city
```

---

## Loop Through Values

```python
for value in person.values():
    print(value)
```

### Output

```text
Alex
10
Delhi
```

---

## Loop Through Keys and Values

The most common approach is `.items()`.

```python
for key, value in person.items():
    print(key, ":", value)
```

### Output

```text
name : Alex
age : 10
city : Delhi
```

---

# Nested Dictionaries

A dictionary can contain another dictionary.

### Example

```python
students = {
    "alex": {
        "age": 10,
        "grade": 5
    },
    "sam": {
        "age": 11,
        "grade": 6
    }
}

print(students["alex"])
print(students["alex"]["age"])
```

### Output

```text
{'age': 10, 'grade': 5}
10
```

---

# Looping Through Nested Dictionaries

```python
students = {
    "alex": {"age": 10, "grade": 5},
    "sam": {"age": 11, "grade": 6}
}

for student_name, info in students.items():
    print(student_name, "is", info["age"], "years old")
```

### Output

```text
alex is 10 years old
sam is 11 years old
```

---

# Dictionary Comprehension

Dictionary comprehensions create dictionaries in a single line.

### Example

```python
squares = {
    x: x * x
    for x in range(5)
}

print(squares)
```

### Output

```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

You'll learn dictionary comprehensions in more detail later.

---

# Common Dictionary Methods

| Method | Description |
|---------|-------------|
| `get(key)` | Safely retrieve a value |
| `keys()` | Get all keys |
| `values()` | Get all values |
| `items()` | Get key-value pairs |
| `pop(key)` | Remove a key and return its value |
| `update()` | Add or update multiple values |
| `len()` | Number of key-value pairs |

---

# Using `update()`

### Example

```python
person = {
    "name": "Alex",
    "age": 10
}

person.update({
    "age": 11,
    "city": "Delhi"
})

print(person)
```

### Output

```text
{'name': 'Alex', 'age': 11, 'city': 'Delhi'}
```

---

# Dictionaries and JSON

If you're interested in web development, dictionaries are one of the most important Python data structures.

API responses are usually sent as **JSON**, which looks almost identical to a Python dictionary.

### Example

```python
api_response = {
    "status": "success",
    "user": {
        "id": 1,
        "name": "Alex",
        "email": "alex@example.com"
    }
}

print(api_response["user"]["name"])
```

### Output

```text
Alex
```

When you learn Flask, FastAPI, or Django, you'll work with dictionaries constantly.

---

# Practice Program

Create a file named **`lesson_dict.py`**.

```python
student = {
    "name": "Alex",
    "age": 10,
    "subjects": ["Math", "Science", "Art"]
}

print(student["name"])
print(student.get("grade", "Not enrolled"))

student["age"] = 11
student["grade"] = 5

print(student)

for key, value in student.items():
    print(key, "->", value)


students = {
    "alex": {
        "age": 10,
        "city": "Delhi"
    },
    "sam": {
        "age": 11,
        "city": "Mumbai"
    }
}

for name, info in students.items():
    print(f"{name.title()} is {info['age']} years old and lives in {info['city']}")


ages = {
    name: info["age"]
    for name, info in students.items()
}

print(ages)
```

### Sample Output

```text
Alex
Not enrolled

{'name': 'Alex', 'age': 11, 'subjects': ['Math', 'Science', 'Art'], 'grade': 5}

name -> Alex
age -> 11
subjects -> ['Math', 'Science', 'Art']
grade -> 5

Alex is 10 years old and lives in Delhi
Sam is 11 years old and lives in Mumbai

{'alex': 10, 'sam': 11}
```

---

# Key Takeaways

- Dictionaries store data as **key-value pairs**.
- Access values using keys instead of indexes.
- Use `.get()` to safely retrieve values.
- Use `del` or `.pop()` to remove items.
- The `in` operator checks dictionary **keys** by default.
- `.items()` is the most common way to loop through keys and values.
- Dictionaries can contain other dictionaries.
- Dictionary comprehensions provide a concise way to build dictionaries.
- Dictionaries are the foundation of JSON and are used extensively in web development.

---

**Next Lesson:** Working with Strings