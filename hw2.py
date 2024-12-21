"""
#evenorodd
num=int(input("Enter a number here:"))
if num % 2 == 0 :
    print("Even")
else:
    print("Odd")

"""
"""
#test marks
print("Question 1: is 6 an odd or even number?")
answer1=input("Enter your answer here")
if answer1.lower() == "even":
    score1=100
else:
    score1=0
print("Question 2: is 4 divisible by 2?")
answer2=input("Enter your answer here")
if answer2.lower() == "yes":
    score2=100
else:
    score2=0
print("Question 3: is 100 divisible by 2?")
answer3=input("Enter your answer here")
if answer3.lower() == "yes":
    score3=100
else:
    score3=0
print("Question 4: is 5 an odd or even number?")
answer4=input("Enter your answer here")
if answer4.capitalize()== "Odd":
    score4=100
else:
    score4=0
print("Question 5: is 10x2=50?")
answer5=input("Enter your answer here")
if answer5.capitalize() == "No":
    score5=100
else:
    score5=0
score=score1+score2+score3+score4+score5
print(score)
if 0<=score<=500:
    if 400<=score<=500:
        print("You got an A")
    elif 300<=score<=399:
        print("You got a B")
    elif 200<=score<=299:
        print("You got a C")
    elif 100<=score<=199:
        print("You got a d")
    else:
        print("You got a F")
else:
    print("Invalid test result")
