##Exceptions and error handling
try:
    with open("app.py") as file:
        print("File opened")
        print(file.read())
    age=int(input("What is your age:"))
    x=10/age
    
except (ValueError,ZeroDivisionError) as ex:
    print("You didnt enter a valid age")
    print(ex)
    print(type(ex))

else:
    print("You entered a valid age")
##finally:  #####It will always be executd even if there is an error






######
def calculate_xfactor(age):
    if age<=0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age
calculate_xfactor(-1)