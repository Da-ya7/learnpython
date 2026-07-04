# LISTS
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.insert(1, "kiwi")
print(fruits)
print(fruits[-1])
print(fruits[1:3])

list_a = [1, 2, 3]
list_b = list_a.copy()
list_b.append(4)
print("list_a:", list_a)
print("list_b:", list_b)

# TUPLES
point = (5, 10)
x, y = point
print(f"x is {x}, y is {y}")

def get_min_max(numbers):
    return (min(numbers), max(numbers))

low, high = get_min_max([4, 7, 1, 9, 2])
print("low:", low, "high:", high)

# SETS
names = ["Alex", "Sam", "Alex", "Jo", "Sam", "Alex"]
unique_names = set(names)
print(unique_names)

math_club = {"Alex", "Sam", "Jo"}
art_club = {"Jo", "Priya", "Sam"}
print("Both clubs:", math_club & art_club)
print("Either club:", math_club | art_club)
print("Math only:", math_club - art_club)