"""
name=input("Enter your name:")
print("Welcome", name, "to Python @ Moonpreneur")

#Area of circle
import math
r=int(input("Enter radius:"))
area=math.pi*r**2
print(f'Area of circle with radius {r} is {area:.2f}')
"""
"""
#Area of triangle
import math
h=int(input("Enter height:"))
b=int(input("Enter base:"))
area= h*b/2
print(f'Area of a triangle with height {h} and base {b} is {area:.1f}')

"""
import time, re
t=time.localtime()
y=int(t.tm_year)
m=int(t.tm_mon)
name=input("Enter your name:").strip()
if len(name)<3 or not re.match("^[a-zA-Z ]+$",name):
    print("name can only contain alphabets and spaces and greater than 3 letters")
try:
    birth_year=int(input("Enter your birth year:"))
except:
    print("Enter a valid birth year")
try:
    birth_month=int(input("Enter your birth month (1-12):"))
except:
    print("Enter a valid birth month")
else:
    age= y-birth_year
    if birth_month > m:
        age = age - 1
    print(f'Your age according to your birth year {birth_year} is {age}')




