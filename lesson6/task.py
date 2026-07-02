def calculate_area(length, width=1):
    area = length * width
    return area

# basic call
print(calculate_area(5, 3))

# using the default value
print(calculate_area(5))

def describe_student(name, **details):
    print(f"Student: {name}")
    for key, value in details.items():
        print(f"  {key}: {value}")

describe_student("Alex", age=10, grade=5, favorite_subject="Math")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

total = 0
def add_to_total(x):
    global total #without using global python ask us to create a local value for total inside the function
    total += x

add_to_total(5)
add_to_total(10)
print(total)
