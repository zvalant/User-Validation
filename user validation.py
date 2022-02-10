def choice():
    number = input("please choose a number between 0-10:") # get user input 
    if number.isdigit() == True and int(number) in range(0, 10): # determine if input is digit and in range   
        return number 
    else:
        print("ERROR: please choose a number between 0-10") # print error statement and return function to retry
        return choice()
print(choice())
