"""
#max
num1=int(input("Enter one number here:"))
num2=int(input("Enter another number here:"))
num3=int(input("Enter a third number here:"))
if num1>num2>num3:
    print(f'the first number {num1} is greater than the second number {num2} and the third number {num3}')
elif num2>num3:
    print(f'the second number {num2} is greater than the third number {num3} and the first number {num1} ')
else:
    print(f'the third number {num3} is greater than the second number {num2} and the first number {num1} ')    
"""
#ATM
balance=100
print("Welcome, please insert the card for assistance")
pin=input("enter your pin:")
if pin=="1234":
    print("Menu")
    print("1.Withdraw\n2.Deposit\n3.Check Balance\n4.Quit\n")
    choice=input("Enter your choice(1-4):")
    if choice=="1":
        amt=float(input("Enter the amount you want to withdraw:"))
        if amt>balance:
            print("Insufficient balance")
        else:
            balance=balance-amt
            print(f"Current balance is {balance}")
    elif choice=="2":
        amt=float(input("Enter the amount you want to deposit:"))
        balance=balance+amt
        print(f"Current balance is {balance}")
    elif choice=="3":
        print(f"Current balance is {balance}")
    elif choice=="4":
        print("Thank you for using this ATM!")
else:
    print("Invalid pin!!!")
