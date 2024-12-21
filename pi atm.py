import math
balance=100+math.pi
def withdraw():
    global balance
    amt=float(input("Enter the amount you want to withdraw:"))
    if amt>balance-10:
        print("Insufficient balance")
    else:
        balance-=amt
        print(f"Current balance is {balance}")
def deposit():
    global balance
    amt=float(input("Enter the amount you want to deposit:"))
    if amt<0:
        print("Invalid amount")
    else:
        balance+=amt
        print(f"Current balance is {balance}")
def menu():
    global balance
    print("Welcome, please insert the card for assistance")
    pin=input("enter your pin:")
    if pin=="1234":
        while True:
            print("Menu")
            print("1.Withdraw\n2.Deposit\n3.Check Balance\n4.Quit\n")
            choice=input("Enter your choice(1-4):")
            if choice=="1":
                withdraw()
            elif choice=="2":
                deposit()
            elif choice=="3":
                print(f"Current balance is {balance}")
            elif choice=="4":
                print("Thank you for using this ATM!")
                break
    else:
        print("Invalid pin!!!")


menu()   
