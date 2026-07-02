def get_age():
    try:
        age=int(input("Enter your age:"))
        if age < 0:
            raise ValueError("Age cannot be negative")
    except ValueError as e:
            print("Invalid input:",e)
            return None
    else:
         print("Thanks you entered a valid age")
         return age
    finally:
         print("Done trying to get age.\n")
result=get_age()
print("Final result",result)
