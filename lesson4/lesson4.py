# Try this WITHOUT casting first (comment out the int() lines to see the error)
age = input("Enter your age: ")
print(type(age))

age = int(age)
print(type(age))
print("Next year you will be:", age + 1)

# float example
price = "19.99"
price = float(price)
print(price * 2)

# str example
number = 100
text = str(number)
print("The number is " + text)