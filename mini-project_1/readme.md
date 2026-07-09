# Mini Project: Secret Code Maker (Caesar Cipher)

[Back to the main roadmap](../README.md) | [Previous lesson: Working with Strings](../lesson10/readme.md)

## Project Goal

Build a program that can:

- Encode (encrypt) a message
- Decode (decrypt) a message
- Keep running until the user chooses to quit

This project combines everything you've learned so far:

- Variables
- Loops
- Functions
- Conditionals
- Strings
- `ord()` and `chr()`
- User input
- `while` loops

---

# Topics Covered

- Encoding and decoding messages with a Caesar cipher
- Shifting letters with `ord()` and `chr()`
- Handling uppercase, lowercase, and non-letter characters
- Building reusable logic with a function
- Repeating work with a `while True` loop
- Reading user input and handling choices

---

# What is a Caesar Cipher?

A **Caesar Cipher** is one of the oldest encryption techniques.

Every letter is shifted by a fixed number.

For example, with a shift of **3**:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

So,

```text
HELLO
```

becomes

```text
KHOOR
```

Only someone who knows the shift value can decode the message.

---

# Understanding `ord()` and `chr()`

Python stores every character as a number.

`ord()` converts a character into its ASCII value.

`chr()` converts an ASCII value back into a character.

### Example

```python
print(ord("A"))
print(ord("a"))

print(chr(65))
print(chr(97))
```

### Output

```text
65
97
A
a
```

Notice:

- Uppercase letters start at **65**
- Lowercase letters start at **97**

---

# Shifting One Letter

Suppose we want to shift the letter **Y** by **3**.

Instead of simply adding `3`, we must wrap around after `Z`.

The formula is:

```python
new_number = (ord(letter) - 65 + shift) % 26 + 65
```

### Example

```python
letter = "Y"
shift = 3

new_number = (ord(letter) - 65 + shift) % 26 + 65
new_letter = chr(new_number)

print(new_letter)
```

### Output

```text
B
```

Why?

```text
Y → Z → A → B
```

The `% 26` operator wraps around the alphabet.

---

# Encoding an Entire Message

Instead of shifting one letter, loop through every character.

### Example

```python
message = "HELLO"
shift = 3

result = ""

for letter in message:
    new_number = (ord(letter) - 65 + shift) % 26 + 65
    new_letter = chr(new_number)

    result += new_letter

print(result)
```

### Output

```text
KHOOR
```

The variable `result` gradually builds the encrypted message.

---

# Handling Spaces and Lowercase Letters

The previous program breaks when it encounters spaces or lowercase letters.

We fix that using conditionals.

### Example

```python
message = "Hi There!"
shift = 3

result = ""

for letter in message:

    if letter.isupper():
        new_number = (ord(letter) - 65 + shift) % 26 + 65
        result += chr(new_number)

    elif letter.islower():
        new_number = (ord(letter) - 97 + shift) % 26 + 97
        result += chr(new_number)

    else:
        result += letter

print(result)
```

### Output

```text
Kl Wkhuh!
```

Notice:

- Uppercase letters stay uppercase.
- Lowercase letters stay lowercase.
- Spaces and punctuation remain unchanged.

---

# Creating a Function

Instead of repeating the same code, put it inside a function.

### Example

```python
def caesar_shift(message, shift):

    result = ""

    for letter in message:

        if letter.isupper():
            new_number = (ord(letter) - 65 + shift) % 26 + 65
            result += chr(new_number)

        elif letter.islower():
            new_number = (ord(letter) - 97 + shift) % 26 + 97
            result += chr(new_number)

        else:
            result += letter

    return result
```

Now we can reuse the function whenever we want.

---

# Encoding

```python
text = "Hello World"

encoded = caesar_shift(text, 3)

print(encoded)
```

### Output

```text
Khoor Zruog
```

---

# Decoding

To decode, simply shift in the opposite direction.

```python
decoded = caesar_shift(encoded, -3)

print(decoded)
```

### Output

```text
Hello World
```

Encoding uses a positive shift.

Decoding uses a negative shift.

---

# Complete Program

```python
def caesar_shift(message, shift):

    result = ""

    for letter in message:

        if letter.isupper():
            new_number = (ord(letter) - 65 + shift) % 26 + 65
            result += chr(new_number)

        elif letter.islower():
            new_number = (ord(letter) - 97 + shift) % 26 + 97
            result += chr(new_number)

        else:
            result += letter

    return result


while True:

    choice = input("Encode, Decode, or Quit? (e/d/q): ").lower()

    if choice == "q":
        print("Bye, secret agent.")
        break

    elif choice == "e":

        text = input("Enter your message: ")

        shift = int(input("Enter shift number: "))

        print("Your secret code:")
        print(caesar_shift(text, shift))

    elif choice == "d":

        text = input("Enter your encoded message: ")

        shift = int(input("Enter shift number: "))

        print("Decoded message:")
        print(caesar_shift(text, -shift))

    else:
        print("Invalid choice. Try again.")
```

---

# Sample Run

```text
Encode, Decode, or Quit? (e/d/q): e

Enter your message:
Hello World

Enter shift number:
3

Your secret code:
Khoor Zruog
```

---

```text
Encode, Decode, or Quit? (e/d/q): d

Enter your encoded message:
Khoor Zruog

Enter shift number:
3

Decoded message:
Hello World
```

---

```text
Encode, Decode, or Quit? (e/d/q): q

Bye, secret agent.
```

---

# Concepts Used

| Concept | Where It Is Used |
|----------|------------------|
| Variables | Store message, shift, result |
| Strings | Encrypt and decrypt text |
| `ord()` | Convert character → number |
| `chr()` | Convert number → character |
| Functions | `caesar_shift()` |
| Loops | Process each character |
| Conditionals | Uppercase, lowercase, or other characters |
| Modulus (`%`) | Wrap around the alphabet |
| `while True` | Keep the program running |
| `break` | Exit the program |
| User Input | Read message and shift |

---

# Challenge Yourself

Try adding these features:

### Level 1

- Allow shifts larger than 26 (e.g., 54, 100).
- *(Hint: `% 26` already makes this work!)*

### Level 2

Add a **Brute Force Mode**.

Instead of asking for the shift, try every possible shift from **1 to 25**.

Example:

```text
Shift 1: Ifmmp
Shift 2: Jgnnq
Shift 3: Khoor
...
Shift 23: Ebiil
Shift 24: Dahhk
Shift 25: Czggj
```

This helps crack messages when you don't know the key.

### Level 3

Keep asking for a valid shift until the user enters a number.

Use `try` and `except` to handle invalid input.

---

# Key Takeaways

- `ord()` converts characters into numbers.
- `chr()` converts numbers back into characters.
- `% 26` wraps letters around the alphabet.
- Functions make code reusable.
- Loops process every character in a message.
- Conditionals handle uppercase, lowercase, and non-letter characters.
- Decoding is simply encoding with a negative shift.
- This project combines many core Python concepts into one practical application.

---

**Next Project Ideas:**

- Password Generator
- Number Guessing Game
- Hangman
- Contact Book (using Dictionaries)
- Student Management System