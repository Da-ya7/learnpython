age=15
has_permission = False

if age>=18:
    print("You are an adult")
elif age>=13 and age <18:
    print("You are a teenager")
else:
    print("You are a kid")

if age>=20 or has_permission == True:
    print("You can watch the Movie")
else:
    print("Sorry,no movie for you")