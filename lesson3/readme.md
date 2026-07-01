# Lesson 3: Conditionals

[Back to the main roadmap](../README.md) | [Previous lesson: Variables and Data Types](../lesson2/readme.md) | [Next lesson: Type Casting](../lesson4/readme.md)

## What are Conditionals?

Conditionals allow your program to **make decisions**.

Think of it like giving instructions to a robot:

> **If** something is true, do one thing.
> **Otherwise**, do something else.

### Real-Life Example

> If it's raining, take an umbrella. Otherwise, don't.

---

# The Building Blocks

Python uses three keywords to make decisions:

* `if`
* `elif`
* `else`

### Example

```python
weather = "rainy"

if weather == "rainy":
    print("Take an umbrella")
elif weather == "sunny":
    print("Wear sunglasses")
else:
    print("Just go outside normally")
```

### Output

```text
Take an umbrella
```

---

## How It Works

Python checks each condition **from top to bottom**.

* `if` → Checks the first condition.
* `elif` → Checks another condition only if the previous one was `False`.
* `else` → Runs if none of the previous conditions were `True`.

Python stops checking as soon as it finds the first `True` condition.

---

# `=` vs `==`

This is one of the most common beginner mistakes.

| Symbol | Meaning                       |
| ------ | ----------------------------- |
| `=`    | Assigns a value to a variable |
| `==`   | Compares two values           |

### Assignment (`=`)

```python
age = 10
```

This stores the value `10` in the variable `age`.

---

### Comparison (`==`)

```python
age = 10

print(age == 10)
print(age == 5)
```

### Output

```text
True
False
```

* `age == 10` asks: **"Is age equal to 10?"**
* `age == 5` asks: **"Is age equal to 5?"**

The answer is either `True` or `False`.

---

# Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
x = 10

print(x > 5)
print(x < 5)
print(x != 8)
```

### Output

```text
True
False
True
```

---

# Combining Conditions

Sometimes you need to check more than one condition.

Python provides three logical operators:

* `and`
* `or`
* `not`

---

## `and`

Both conditions must be `True`.

### Example

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter")
else:
    print("You cannot enter")
```

### Output

```text
You can enter
```

---

## `or`

At least one condition must be `True`.

### Example

```python
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No school today")
```

### Output

```text
No school today
```

---

## `not`

Reverses a Boolean value.

### Example

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

### Output

```text
Please log in
```

---

# Practice Program

Create a file named **`lesson3.py`** and write the following code.

```python
age = 15
has_permission = False

if age >= 18:
    print("You are an adult")
elif age >= 13 and age < 18:
    print("You are a teenager")
else:
    print("You are a kid")

if age >= 13 or has_permission:
    print("You can watch the movie")
else:
    print("Sorry, no movie for you")
```

### Output

```text
You are a teenager
You can watch the movie
```

### Why?

* `age` is **15**, so it is not greater than or equal to **18**.
* It is greater than or equal to **13**, so Python prints **"You are a teenager."**
* The second condition uses `or`.
* Since `age >= 13` is already `True`, Python prints **"You can watch the movie."**
* It doesn't matter that `has_permission` is `False` because `or` only needs one condition to be `True`.

---

# Try It Yourself

Change the values:

```python
age = 20
has_permission = True
```

### What happens?

The output becomes:

```text
You are an adult
You can watch the movie
```

**Why?**

* `age >= 18` is now `True`, so Python prints **"You are an adult."**
* Both `age >= 13` and `has_permission` are `True`, so the second message remains **"You can watch the movie."**

---

# Key Takeaways

* Conditionals allow programs to make decisions.
* `if` checks the first condition.
* `elif` checks another condition if the previous one was `False`.
* `else` runs when no conditions are `True`.
* `=` assigns a value, while `==` compares values.
* Use comparison operators to ask questions about values.
* `and` requires all conditions to be `True`.
* `or` requires at least one condition to be `True`.
* `not` reverses a Boolean value.

[Back to the main roadmap](../README.md) | [Previous lesson: Variables and Data Types](../lesson2/readme.md) | [Next lesson: Type Casting](../lesson4/readme.md)

---

**Next Lesson:** Type Casting
