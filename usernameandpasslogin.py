username=input("Make your first username here: ")
print("Username saved!")
password=int(input("Make your first password here, numbers only: "))
print("Password saved!Please log in.")
user=input("Enter your username here: ")
if user==username:
    try:
        pas=int(input("Enter your password here: "))
    except ValueError:
        print("Input a valid password")
    else:
        if pas==password:
            print("You have successfully logged in")
        else:
            print("Login Failed.")
else:
    print("Login Failed.")
        

    
    
