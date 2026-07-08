name = "  Python Programming  "

# 1. Clean it up
clean_name = name.strip()
print(f"'{clean_name}'")

# 2. Case methods
print(clean_name.upper())
print(clean_name.lower())

# 3. Slicing
print(clean_name[0:6])
print(clean_name[::-1])

# 4. f-strings with logic
age = 10
years_until_18 = 18 - age
print(f"You have {years_until_18} years until you're 18")

# 5. split and join
sentence = "I love learning Python"
words = sentence.split()
print(words)
print(len(words))
reversed_sentence = " ".join(words[::-1])
print(reversed_sentence)

# 6. searching
review = "This course is amazing and well explained"
print("amazing" in review)
print(review.find("well"))
print(review.count("a"))

# 7. validation practice
user_input = "12a5"
if user_input.isdigit():
    print("Valid number:", int(user_input))
else:
    print("Invalid number entered")