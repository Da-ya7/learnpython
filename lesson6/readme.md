# Lesson 6: Functions & Built-in Functions

[Back to the main roadmap](../README.md) | [Previous lesson: Exceptions](../lesson5/readme.md)

## What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, you write it once inside a function and call it whenever you need it.

---

## Real-Life Example

Think of a **coffee machine**.

You don't rebuild the machine every time you want coffee.

You simply press a button, and the machine performs the same steps every time:

- Grind the beans
- Brew the coffee
- Pour the coffee

Functions work the same way.

---

# Defining a Function

Use the `def` keyword to create a function.

### Example

```python
def make_coffee():
    print("Grinding beans...")
    print("Brewing...")
    print("Coffee is ready!")

make_coffee()
make_coffee()
```

### Output

```text
Grinding beans...
Brewing...
Coffee is ready!
Grinding beans...
Brewing...
Coffee is ready!
```

---

## Understanding the Syntax

```python
def make_coffee():
```

- `def` → Defines a function.
- `make_coffee` → Function name.
- `()` → Parentheses for inputs (parameters).
- `:` → Starts the function body.
- Indented lines → Code that belongs to the function.

A function does **nothing** until you call it.

---

# Parameters and Arguments

Functions become much more useful when they can receive data.

### Example

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alex")
greet("Sam")
```

### Output

```text
Hello, Alex!
Hello, Sam!
```

### Explanation

- `name` is a **parameter**.
- `"Alex"` and `"Sam"` are **arguments**.

Think of the parameter as an empty box that gets filled when the function is called.

---

# Multiple Parameters

Functions can accept more than one input.

### Example

```python
def introduce(name, age):
    print(name + " is " + str(age) + " years old.")

introduce("Alex", 10)
```

### Output

```text
Alex is 10 years old.
```

Arguments are matched by their position.

---

# Keyword Arguments

Instead of relying on position, you can specify parameter names.

### Example

```python
introduce(age=10, name="Alex")
```

The output is exactly the same.

Using keyword arguments makes code easier to read and allows the arguments to be written in any order.

---

# `return` vs `print`

This is one of the most important concepts in Python.

## `print()`

Displays information on the screen.

```python
def add_print(a, b):
    print(a + b)

add_print(3, 5)
```

### Output

```text
8
```

The value is displayed but **not returned**.

---

## `return`

Returns a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(3, 5)

print(result)
```

### Output

```text
8
```

The returned value can be stored in a variable or used later.

---

## Comparing `print` and `return`

```python
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(3, 5)
y = add_return(3, 5)

print(x)
print(y)
```

### Output

```text
8
None
8
```

### Why?

- `add_print()` only displays the value.
- It doesn't return anything.
- Python automatically returns `None` when there is no `return` statement.
- `add_return()` returns the value `8`.

Remember:

- `print()` **shows**
- `return` **gives back**

---

# A Function Stops at `return`

When Python reaches a `return` statement, the function ends immediately.

```python
def check_age(age):
    if age < 0:
        return "Invalid age"

    return "Valid age"

    print("This never runs.")
```

The last `print()` is never executed because the function has already finished.

---

# Default Parameter Values

Parameters can have default values.

### Example

```python
def greet(name="friend"):
    print("Hello, " + name + "!")

greet()
greet("Alex")
```

### Output

```text
Hello, friend!
Hello, Alex!
```

If no argument is supplied, Python uses the default value.

---

# `*args`

Sometimes you don't know how many arguments will be passed.

Use `*args`.

### Example

```python
def add_all(*numbers):
    total = 0

    for n in numbers:
        total += n

    return total

print(add_all(1, 2, 3))
print(add_all(1, 2, 3, 4, 5))
```

### Output

```text
6
15
```

`*numbers` collects all positional arguments into a tuple.

---

# `**kwargs`

Sometimes you don't know the names of the arguments either.

Use `**kwargs`.

### Example

```python
def describe_person(**info):
    for key, value in info.items():
        print(key + ":", str(value))

describe_person(
    name="Alex",
    age=10,
    city="Delhi"
)
```

### Output

```text
name: Alex
age: 10
city: Delhi
```

`**kwargs` stores named arguments inside a dictionary.

---

# Variable Scope

Variables created inside a function only exist inside that function.

### Example

```python
def my_function():
    x = 5
    print(x)

my_function()

print(x)
```

### Output

```text
5
NameError: name 'x' is not defined
```

`x` is a **local variable**.

It disappears after the function finishes.

---

# Global Variables

Variables created outside functions are called **global variables**.

### Example

```python
count = 0

def increase():
    global count
    count += 1

increase()

print(count)
```

### Output

```text
1
```

The `global` keyword tells Python to use the variable outside the function.

---

# Built-in Functions

Python includes many useful functions that are always available.

| Function | Purpose | Example |
|----------|---------|---------|
| `print()` | Display output | `print("Hello")` |
| `input()` | Read user input | `input("Name: ")` |
| `len()` | Count items | `len("hello") → 5` |
| `type()` | Get data type | `type(5)` |
| `int()` | Convert to integer | `int("25")` |
| `float()` | Convert to float | `float("3.14")` |
| `str()` | Convert to string | `str(25)` |
| `max()` | Largest value | `max(2, 5, 1)` |
| `min()` | Smallest value | `min(2, 5, 1)` |
| `sum()` | Sum numbers | `sum([1,2,3])` |
| `sorted()` | Sort items | `sorted([3,1,2])` |
| `range()` | Generate numbers | `range(5)` |
| `abs()` | Absolute value | `abs(-5)` |

You don't need to memorize them all.

You'll naturally learn them as you continue programming.

---

# Practice Program

Create a file named **`lesson6.py`**.

```python
def calculate_area(length, width=1):
    area = length * width
    return area


# Basic call
print(calculate_area(5, 3))

# Using the default value
print(calculate_area(5))


def describe_student(name, **details):
    print(f"Student: {name}")

    for key, value in details.items():
        print(f"  {key}: {value}")


describe_student(
    "Alex",
    age=10,
    grade=5,
    favorite_subject="Math"
)


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))


total = 0

def add_to_total(x):
    global total
    total += x


add_to_total(5)
add_to_total(10)

print(total)
```

### Output

```text
15
5
Student: Alex
  age: 10
  grade: 5
  favorite_subject: Math
5.0
Cannot divide by zero
15
```

---

# Key Takeaways

- Functions let you reuse code.
- Use `def` to create a function.
- Call a function using its name followed by `()`.
- Parameters receive values from arguments.
- `return` sends a value back.
- `print()` displays output but does not return it.
- A function ends immediately when it reaches `return`.
- Default parameters provide fallback values.
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple named arguments.
- Local variables exist only inside functions.
- Global variables exist outside functions and can be modified using `global`.
- Python provides many built-in functions like `print()`, `len()`, `sum()`, and `sorted()`.

---

[Back to the main roadmap](../README.md) | [Previous lesson: Exceptions](../lesson5/readme.md)