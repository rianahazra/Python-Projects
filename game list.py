import random
list=["cat", "dog", "fox", "rat", "bat", "gnat", "cow", "goat", "pig","crow"]

word_to_guess=random.choice(list) #gnat _ _ a _
len_word="_ "*len(word_to_guess) #4
chances=3
while chances>0:
    user_input=input(f"enter a word {len_word}:")
    if user_input == word_to_guess:
        print("You won")
        break 
    else:
        print("Try again")
        chances=chances-1
        print(chances)
        if chances==0:
            print("You lost")
