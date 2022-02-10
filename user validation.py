def choice():
    number = input("please choose a number between 0-10:")
    if number.isdigit() == True and int(number) in range(0, 10):
        return number
    else:
        print("ERROR: please choose a number between 0-10")
        return choice()
print(choice())