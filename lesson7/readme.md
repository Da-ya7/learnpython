# Lesson 7: Loops

[Back to the main roadmap](../README.md) | [Previous lesson: Functions & Built-in Functions](../lesson6/readme.md)

## What is a Loop?

A **loop** lets you repeat a block of code without writing it over and over again.

Instead of writing:

```python
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
```

You can simply tell Python:

> Repeat this 5 times.

---

## Real-Life Example

Imagine washing **10 dishes**.

You don't invent a new set of instructions for every dish.

You simply repeat the same steps:

- Pick up the dish
- Scrub it
- Rinse it
- Put it away

A loop works the same way.

---

# Types of Loops

Python has two main types of loops:

- `for` loop
- `while` loop

---

# `for` Loop

A `for` loop goes through items one at a time.

### Example

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
apple
banana
cherry
```

### How It Works

Python reads it like this:

- Take the first item → `"apple"`
- Store it in `fruit`
- Run the code inside the loop
- Repeat for every remaining item

After the last item, the loop ends automatically.

---

# Looping Through a String

Strings are collections of characters.

Python can loop through each character.

### Example

```python
for letter in "cat":
    print(letter)
```

### Output

```text
c
a
t
```

---

# Using `range()`

The `range()` function generates numbers.

### Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

Notice that `5` is **not included**.

`range(5)` produces **five numbers**, starting from **0**.

---

## Different Forms of `range()`

### Example

```python
range(5)
```

Output

```text
0 1 2 3 4
```

---

```python
range(2, 6)
```

Output

```text
2 3 4 5
```

---

```python
range(0, 10, 2)
```

Output

```text
0 2 4 6 8
```

The third value is called the **step**.

---

# Using the Loop Variable

The variable inside the loop changes every iteration.

### Example

```python
for i in range(5):
    print("Round:", i)
```

### Output

```text
Round: 0
Round: 1
Round: 2
Round: 3
Round: 4
```

---

# Using `range(len())`

Sometimes you need the position (index) instead of the item.

### Example

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, "-", fruits[i])
```

### Output

```text
0 - apple
1 - banana
2 - cherry
```

Here:

- `i` is the index.
- `fruits[i]` gets the item at that position.

---

# Using `enumerate()`

`enumerate()` gives both the index and the item.

### Example

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, "-", fruit)
```

### Output

```text
0 - apple
1 - banana
2 - cherry
```

This is cleaner than using `range(len())`.

---

# `while` Loop

A `while` loop keeps running **as long as a condition is True**.

### Example

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### Output

```text
0
1
2
3
4
```

### How It Works

- Check if `count < 5`
- If True, run the loop
- Increase `count`
- Check the condition again
- Stop when the condition becomes False

---

# Infinite Loops

If you forget to update the condition, the loop never ends.

### Incorrect Example

```python
count = 0

while count < 5:
    print(count)
```

Since `count` never changes, the condition is always True.

The loop runs forever.

To stop an infinite loop in the terminal, press:

```text
Ctrl + C
```

---

# `while True`

Sometimes you intentionally want a loop to run forever until the user decides to stop.

### Example

```python
while True:
    answer = input("Type 'quit' to stop: ")

    if answer == "quit":
        break

    print("You typed:", answer)
```

The loop stops only when `break` is executed.

---

# `break`

`break` immediately exits the loop.

### Example

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

### Output

```text
0
1
2
3
4
```

When `i` becomes `5`, the loop ends immediately.

---

# `continue`

`continue` skips the current iteration and moves to the next one.

### Example

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

### Output

```text
0
1
3
4
```

The number `2` is skipped.

---

# `break` vs `continue`

| Keyword | What It Does |
|----------|--------------|
| `break` | Stops the loop completely |
| `continue` | Skips only the current iteration |

---

# Nested Loops

A nested loop is a loop inside another loop.

### Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

### Output

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

The inner loop runs completely for every iteration of the outer loop.

---

# `else` with Loops

A loop can also have an `else` block.

The `else` block executes only if the loop finishes normally (without `break`).

### Example

```python
for i in range(5):
    print(i)

else:
    print("Loop finished normally.")
```

### Output

```text
0
1
2
3
4
Loop finished normally.
```

---

# Practice Program

Create a file named **`lesson_loops.py`**.

```python
# 1. Basic for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# 2. range()
for i in range(1, 6):
    print("Count:", i)

# 3. enumerate()
for i, fruit in enumerate(fruits):
    print(i, "-", fruit)

# 4. while loop
count = 0

while count < 5:
    print("While count:", count)
    count += 1

# 5. break and continue
for i in range(10):

    if i == 7:
        break

    if i % 2 == 0:
        continue

    print("Odd number:", i)

# 6. Nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

### Output

```text
apple
banana
cherry

Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

0 - apple
1 - banana
2 - cherry

While count: 0
While count: 1
While count: 2
While count: 3
While count: 4

Odd number: 1
Odd number: 3
Odd number: 5

1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

---

# Key Takeaways

- Loops repeat code automatically.
- Python has two loop types: `for` and `while`.
- Use `for` when looping through a sequence.
- Use `while` when repeating until a condition becomes False.
- `range()` generates a sequence of numbers.
- `enumerate()` provides both the index and the value.
- `break` exits the loop immediately.
- `continue` skips the current iteration.
- Nested loops are loops inside other loops.
- A loop's `else` block runs only if the loop completes without `break`.

---

**Next Lesson:** Lists, Tuples, and Sets