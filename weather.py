"""
#temperature
celcius=int(input("Enter celcius: "))
if 0<celcius<10:
    print("good weather")
    
elif 10<celcius<20:
    print("normal weather")

else:
    print("bad weather")
"""
"""
#define two numbers
num1=10
num2=20

#Use comparison operators to compare the numbers
print((num1>num2)-(num1<num2))

"""
"""
#define two variables
x=6
y=9

#compare the variables using comparison operators
greater_than=x>y
less_than=x<y
equal_to=x==y

#print the results
print("Is x greater than y?", greater_than) #will print false
print("Is x less than y?", less_than) #will print true
print("is x equal to y?", equal_to) #will print false
"""
"""
#google account username and password
username=input("Enter your username:")
password=input("Enter your password:")
if username=="abc123@gmail.com":
    if password=="abc123":
        print("Welcome to gmail")
    else:
        print("Wrong password try again")

else:
    print("Username is wrong")
    if password != "abc123":
        print("Password is wrong")
"""

#test marks
test=int(input("Enter your marks here:"))
if 0<=test<=100:
    if 90<=test<=100:
        print("You got an A")
    elif 80<=test<=89:
        print("You got a B")
    elif 70<=test<=79:
        print("You got a C")
    elif 60<=test<=69:
        print("You got a d")
    else:
        print("You got a F")
else:
    print("Invalid test result")



