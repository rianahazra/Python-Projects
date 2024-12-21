#armstrong numbers
num1=int(input("Enter number 1 here: "))
num2=int(input("Enter number 2 here: "))
num3=int(input("Enter number 3 here: "))
formula= num1**3+num2**3+num3**3
if str(formula)== str(num1)+str(num2)+str(num3):
    print("Armstrong number")
else:
    print("no arm")
    
