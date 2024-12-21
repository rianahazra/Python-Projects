import random
attempts=0
word_list=["bulk","tour", "trip", "four"]
correct=random.choice(word_list)
choice=""
while choice != correct:
    bulls=0
    cows=0
    attempts+=1
    choice=input("Enter a four letter word here, no repeats").lower()
    print(len(choice))
    if len(choice) != 4:
        print("Please input exactly 4 letters")
        continue
    for i in range (4):
        if choice[i]==correct[i]:
            bulls+=1
    for i in range (4):
        if correct[i] in choice and choice[i] != correct[i]:
            cows+=1
    if bulls==4:
        print(f'Congratulations you guessed right with this many attempts {attempts}')
        break
    print(f'the number of bulls are {bulls}')
    print(f'the number of cows are {cows}')
    print(f'the number of attempts are {attempts}')

    
            
    
