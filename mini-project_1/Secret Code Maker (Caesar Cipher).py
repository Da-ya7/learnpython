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
    choice=input("Encode,Decode,or Quit? (e/d/q): ")
    
    if choice == "q":
        print("Bye,Secret agent")
        break
    elif choice == "e":
        text=input("Enter your messgae:")
        shift=int(input("Enter the shift:"))
        print("Your secret code: ",caesar_shift(text, shift))
    elif choice == "d":
        text=input("Enter your  messgae:")
        shift=int(input("Enter the shift:"))
        print("Your decoded message: ",caesar_shift(text, -shift))
    else:
        print("Invalid code pls try again")


