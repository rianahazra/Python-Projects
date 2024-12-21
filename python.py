import math
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    try:   
        result= a/b
    except:
        return("Zerodivisionerror")
    else:
        return(result) 
try: 
    num1=int(input("Enter a number here: "))
    num2=int(input("Enter a number here: "))
    print(addition(num1,num2))
    print(subtraction(num1,num2))
    print(multiplication(num1,num2))
    print(division(num1,num2))
except ValueError: 
    print("Please enter a valid number")


