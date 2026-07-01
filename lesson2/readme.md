# Lesson 2: Variables and Data Types

[Back to the main roadmap](../README.md) | [Previous lesson: Basic Syntax](../lesson1/readme.md) | [Next lesson: Conditionals](../lesson3/readme.md)

## What is a Variable?

Think of a variable as a **labeled box**.

You can store something inside the box and give it a name so you can use it later.

### Example

```python
age = 10
```

Here:

* `age` is the name of the box.
* `10` is the value stored inside the box.

You can access the value anytime.

```python
age = 10
print(age)
```

### Output

```text
10
```

---

## Variables Can Change

The value stored in a variable can be changed at any time.

### Example

```python
age = 10
age = 11

print(age)
```

### Output

```text
11
```

The old value (`10`) is replaced by the new value (`11`).

---

# Data Types

Different kinds of values are stored using different **data types**.

| Data Type | Description                 | Example             |
| --------- | --------------------------- | ------------------- |
| `int`     | Whole numbers               | `age = 10`          |
| `float`   | Numbers with decimal points | `height = 4.5`      |
| `str`     | Text (String)               | `name = "Alex"`     |
| `bool`    | Only `True` or `False`      | `is_student = True` |

---

## Integer (`int`)

Stores whole numbers.

### Example

```python
age = 10
print(age)
```

### Output

```text
10
```

---

## Float (`float`)

Stores decimal numbers.

### Example

```python
height = 4.5
print(height)
```

### Output

```text
4.5
```

---

## String (`str`)

Stores text.

Strings are written inside **single quotes (' ')** or **double quotes (" ")**.

### Example

```python
name = "Alex"
print(name)
```

### Output

```text
Alex
```

---

## Boolean (`bool`)

A Boolean can have only one of two values:

* `True`
* `False`

### Example

```python
is_student = True
print(is_student)
```

### Output

```text
True
```

---

# Python Automatically Detects the Data Type

Python is smart enough to determine the data type based on the value you assign.

You don't need to specify the type yourself.

### Example

```python
age = 10
height = 5.8
name = "Alex"
is_student = True
```

Python automatically understands:

* `10` → `int`
* `5.8` → `float`
* `"Alex"` → `str`
* `True` → `bool`

---

# Checking the Data Type

Use the `type()` function to find the data type of a variable.

### Example

```python
age = 10

print(type(age))
```

### Output

```text
<class 'int'>
```

Another example:

```python
name = "Alex"

print(type(name))
```

[Back to the main roadmap](../README.md) | [Previous lesson: Basic Syntax](../lesson1/readme.md) | [Next lesson: Conditionals](../lesson3/readme.md)

### Output

```text
<class 'str'>
```

---

# Variable Naming Rules

Follow these rules when naming variables.

### ✅ Rule 1: No Spaces

```python
# Correct
my_age = 20

# Incorrect
my age = 20
```

---

### ✅ Rule 2: Cannot Start with a Number

```python
# Correct
age1 = 20

# Incorrect
1age = 20
```

---

### ✅ Rule 3: Variable Names are Case-Sensitive

```python
age = 20
Age = 30

print(age)
print(Age)
```

### Output

```text
20
30
```

`age` and `Age` are considered **two different variables**.

---

# Key Takeaways

* A variable is a named container used to store data.
* Variables can be updated by assigning a new value.
* Python has four common data types:

  * `int`
  * `float`
  * `str`
  * `bool`
* Use `type()` to check the data type of a variable.
* Variable names cannot contain spaces or start with numbers.
* Python is case-sensitive (`age` and `Age` are different).

---

**Next Lesson:** Conditionals
