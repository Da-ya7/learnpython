# 1. Basic for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. range()
for i in range(1, 6):
    print("Count:", i)

# 3. enumerate
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
    if i % 2 == 0:   # % means "remainder" — even number check
        continue
    print("Odd number:", i)

# 6. nested loop — simple multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")