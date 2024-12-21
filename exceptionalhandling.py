try:
    user=int(input("Enter a number here"))
except ValueError:
    print("Input a Valid integer")
else: #no error then it goes to else
    square=user**2
    print(square)
finally: #always
    print("you did it")
