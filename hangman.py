
import random
themes=["animals","insects"]
print(themes)
user_input=input(f'Enter a theme')
if user_input==themes[0]:
    list=["cat"]
    word_to_guess=random.choice(list)
    len_word="_ "*len(word_to_guess)
    chances=3
    print(len_word)
    while chances>0:
        if word_to_guess=="cat":
            listcat=["c", "a", "t"]
            user_input=input(f'Guess the first letter from A-Z')
            if user_input=='c' or user_input=='a' or user_input=='t':
                user_input=input(f'Guess the second letter from A-Z')
                if user_input==listcat('a'):
                    user_input=input(f'Guess the third letter from A-Z')
                    if user_input==listcat('t'):
                         print("You won")
                         break
                    else:
                        print("Try again")
                        chances=chances-1
                        print(chances)
                        if chances==0:
                            print("You lost")
                else:
                    print("Try again")
                    chances=chances-1
                    print(chances)
                    if chances==0:
                        print("You lost")
            else:
                print("Try again")
                chances=chances-1
                print(chances)
                if chances==0:
                    print("You lost")
if user_input==themes[1]:
        list=["fly"]
        word_to_guess=random.choice(list)
        len_word="_ "*len(word_to_guess)
        chances=3
        print(len_word)
        while chances>0:
            if word_to_guess=="fly":
                listf=["f", "l", "y"]
                user_input=input(f'Guess the first letter from A-Z')
                if user_input==listf('f'):
                    user_input=input(f'Guess the second letter from A-Z')
                    if user_input==listf('l'):
                        user_input=input(f'Guess the third letter from A-Z')
                        if user_input==listf('y'):
                            print("You won")
                            break
                        else:
                            print("Try again")
                            chances=chances-1
                            print(chances)
                            if chances==0:
                                print("You lost")
                    else:
                        print("Try again")
                        chances=chances-1
                        print(chances)
                        if chances==0:
                            print("You lost")
                else:
                    print("Try again")
                    chances=chances-1
                    print(chances)
                    if chances==0:
                        print("You lost")
