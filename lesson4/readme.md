# Lesson 4: Type Casting

[Back to the main roadmap](../README.md) | [Previous lesson: Conditionals](../lesson3/readme.md)

## What is Type Casting?

Sometimes a variable contains one type of data, but you need it in another type.

**Type casting** is the process of converting one data type into another.

---

## Real-Life Example

Imagine you ask someone their age on a form.

They type:

```text
25
```

Although it looks like a number, Python treats it as **text (a string)**.

If you try to do math with it, Python will raise an error.

### Example

```python
age = "25"

print(age + 5)
```

### Output

```text
TypeError: can only concatenate str (not "int") to str
```

Why?

* `"25"` is a **string**
* `5` is an **integer**
* Python cannot add text and numbers together.

---

# Casting Functions

Python provides built-in functions to convert one data type into another.

| Function  | Converts To | Example              |
| --------- | ----------- | -------------------- |
| `int()`   | Integer     | `int("25") → 25`     |
| `float()` | Float       | `float("4.5") → 4.5` |
| `str()`   | String      | `str(25) → "25"`     |
| `bool()`  | Boolean     | `bool(1) → True`     |

---

# Converting a String to an Integer

### Example

```python
age = "25"

age = int(age)

print(age + 5)
```

### Output

```text
30
```

Now Python knows that `25` is a number, so addition works correctly.

---

# Converting to Float

### Example

```python
price = "19.99"

price = float(price)

print(price * 2)
```

### Output

```text
39.98
```

The string `"19.99"` is converted into the floating-point number `19.99`.

---

# Converting to String

Sometimes you need to convert a number into text.

### Example

```python
number = 100

text = str(number)

print("The number is " + text)
```

### Output

```text
The number is 100
```

Without `str()`, Python would raise an error because you cannot join a string and an integer using `+`.

---

# Converting to Boolean

The `bool()` function converts values into either `True` or `False`.

### Example

```python
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
```

### Output

```text
True
False
False
True
```

Generally:

* `0` → `False`
* Empty string (`""`) → `False`
* Non-zero numbers → `True`
* Non-empty strings → `True`

---

# `input()` Always Returns a String

One of the most common beginner mistakes is forgetting that `input()` always returns **text**, even if the user types a number.

### Example

```python
age = input("How old are you? ")

print(type(age))
```

### Sample Input

```text
21
```

### Output

```text
<class 'str'>
```

Even though you typed `21`, Python stores it as a string.

To perform calculations, convert it to an integer.

```python
age = int(age)

print(age + 1)
```

### Output

```text
22
```

---

[Back to the main roadmap](../README.md) | [Previous lesson: Conditionals](../lesson3/readme.md)

# Practice Program

Create a file named **`lesson4.py`** and write the following code.

```python
# Try this WITHOUT casting first
# (Comment out the int() line to see the error.)

age = input("Enter your age: ")

print(type(age))

age = int(age)

print(type(age))
print("Next year you will be:", age + 1)

# Float example
price = "19.99"
price = float(price)

print(price * 2)

# String example
number = 100
text = str(number)

print("The number is " + text)
```

### Sample Input

```text
18
```

### Output

```text
<class 'str'>
<class 'int'>
Next year you will be: 19
39.98
The number is 100
```

---

# Common Beginner Mistake

```python
age = input("Enter your age: ")

print(age + 1)
```

### Output

```text
TypeError
```

Why?

Because `input()` returns a **string**, not an integer.

The correct way is:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

---

# Key Takeaways

* Type casting converts one data type into another.
* `int()` converts to integers.
* `float()` converts to decimal numbers.
* `str()` converts values into text.
* `bool()` converts values into `True` or `False`.
* `input()` always returns a string.
* Convert user input before performing mathematical operations.

---

**Next Lesson:** Exceptions (Handling Errors)
