'''
print("for")
for i in range(10,0,-1):
    print(i)

print("while")
i=10
while(i>0):
    print(i)
    i=i-1
    
print("program1")
num=int(input("Enter a number:"))
while(num!=0):
    num=int(input("Enter a number:"))
print("Good Job")
'''
'''
import random
computerchoice=(random.randint(1,9))
count=1
#from random import *
playerchoice=int(input("Enter a number:"))
while(playerchoice!=computerchoice):
    print("Wrong Guess")
    playerchoice=int(input("Enter a number:"))
    count=count+1
print(f'The amount of guesses you made to get the correct number is {count}')
    
'''
num=0
while(num<20):
    num=num+1
    if num%2==0:
        print(f"{num} is an Even number")
    else:
        print(f"{num} is an Odd number")
