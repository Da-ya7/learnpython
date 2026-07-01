# Lesson 1: Basic Syntax

[Back to the main roadmap](../README.md) | [Next lesson: Variables and Data Types](../lesson2/readme.md)

Python is like giving instructions to a robot friend.

You don't need to write complicated code. Just write simple instructions, one line at a time, and Python executes them from **top to bottom**.

---

## 1. `print()` — Make the Robot Talk

The `print()` function displays text or values on the screen.

### Example

```python
print("Hello, I am learning Python")
```

### Output

```text
Hello, I am learning Python
```

**Explanation:**

Whatever you put inside `print()` is displayed on the screen.

---

## 2. Comments — Notes for Humans

Comments are used to explain your code. Python ignores comments when running the program.

### Example

```python
# This is a comment. Python ignores this line completely.
print("This line actually runs")
```

### Output

```text
This line actually runs
```

**Explanation:**

* Start a comment with `#`.
* Comments help you remember why you wrote a piece of code.
* They make your code easier for others (and your future self) to understand.

---

## 3. Indentation — Python's Most Important Rule

Unlike many programming languages, **indentation is part of Python's syntax**.

### Example

```python
if 5 > 3:
    print("Five is bigger")
```

### Output

```text
Five is bigger
```

**Explanation:**

The four spaces before `print()` tell Python that this line belongs inside the `if` block.

Think of it like placing a small box inside a larger box.

```
if
└── print()
```

If the indentation is incorrect, Python raises an error.

**Correct**

```python
if 5 > 3:
    print("Five is bigger")
```

**Incorrect**

```python
if 5 > 3:
print("Five is bigger")
```

This produces an **IndentationError** because the `print()` statement is not properly indented.

---

## Key Takeaways

* `print()` displays output on the screen.
* `#` creates comments that Python ignores.
* Indentation defines code blocks and is required in Python.
* Python executes code from **top to bottom**.

---

**Next Lesson:** Variables and Data Types

[Back to the main roadmap](../README.md) | [Next lesson: Variables and Data Types](../lesson2/readme.md)
