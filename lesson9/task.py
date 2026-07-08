student = {
    "name": "Alex",
    "age": 10,
    "subjects": ["Math", "Science", "Art"]
}

print(student["name"])
print(student.get("grade", "Not enrolled"))

student["age"] = 11
student["grade"] = 5
print(student)

for key, value in student.items():
    print(key, "->", value)

students = {
    "alex": {"age": 10, "city": "Delhi"},
    "sam": {"age": 11, "city": "Mumbai"}
}

for name, info in students.items():
    print(f"{name.title()} is {info['age']} years old and lives in {info['city']}")

ages = {name: info["age"] for name, info in students.items()}
print(ages)