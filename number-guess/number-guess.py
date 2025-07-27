#Made by Jean
#Objectives :
#-Pick a number between 1 and 100 CHECK
#-Make a loop that ends when User found the right number CHECK
#-Tell User evidences like "Too big !", "Too tiny !" CHECK
#-Let the User choose level of difficulty CHECK
#-If User exceed 30 attempts he losts CHECK

import random
import string

#Function to launch the game
def guess_number():
    #Make a list of all possible numbers
    numbers = list(range(1,100))

    #Picking the number to guess by calling 'random'
    number_to_guess = random.choice(numbers)

    #State of the User, if he finds the right answer then it becomes True
    found = False

    #Counting the attempts
    user_attempt = 0

    #Level chosen by User
    level = 0

    #Launch input User choose the difficulty of the game
    level = input("" \
    "Hi ! Welcome to the Guess Number Game !\n" \
    "For now, let's start by choosing which level you wanna play :\n" \
    "1. Easy : Guess between 1 and 100, I'll tell you advices ;)\n" \
    "2. Medium : Guess here between 1 and 1.000, I'll still tell advices don't worry :)\n" \
    "3. Hard : Still guess between 1 and 1.000, but I won't give advices anymore, and remember, only 30 attempts :-)\n" \
    "4. IMPOSSIBLE : Here guess between 1 and 1.000.000, you'll have 1 chance, no more no less, so may the luck be with you !\n")

    #If no level has been chosen it will be asked to choose one
    if int(level) < 1 and int(level) > 4:
        chosen_level = False
        while chosen_level == False:
            level = input("Wrong man, 1, 2, 3 or 4, is that so hard ?\n" \
            "SO, which level do you pick ?\n")
            if int(level) > 0 and int(level) < 5:
                chosen_level = True

    #Level 1
    if int(level) == 1:
        #Making an input so User can pick a number
        user_choice = input("Ok so, guess my number...")
        #A While loop that continue as long as the User don't find the answer
        while found == False:
            if user_attempt <= 30 :
                #Tell the user to choose a number only between 1 and 100
                if int(user_choice) > 100 or int(user_choice) < 1:
                    user_choice = input('Hey there, I said between 1 and 100 ! Try again and give me something in that range ;)\n')
                    user_attempt += 1
                #Tell the User that he picked a number superior as the answer
                elif int(user_choice) > number_to_guess:
                    user_choice = input('Nice try but... TOO BIGGG\nTry againnn\n')
                    user_attempt += 1
                #Tell the User that he picked a number inferior as the answer
                elif int(user_choice) < number_to_guess:
                    user_choice = input("Ouch... TOO TINYYYYY\nMaybe this time you'll be better !\n")
                    user_attempt += 1
                else:
                    #If the User finds it in one shot
                    if user_attempt == 0:
                        print(f"HOLY SHIIIIIIIIIT, {user_attempt} ATTEMPTS ??? YOU MUST BE KIDDING ME HOW IS THAT EVEN POSSIBLEEE\nThe right answer was : {number_to_guess}")
                        found = True
                    #If the User finds it in less than 5 attempts
                    elif user_attempt < 5:
                        print(f"GOOD JOB BROOOOOOOOOO, {user_attempt} attempts, really nice job !\nThe right answer was : {number_to_guess}")
                        found = True
                    #If the User finds it in less than 15 attempts
                    elif user_attempt < 15:
                        print(f"Well done well done, {user_attempt} attempts, I guess that's not too bad lol\nThe right answer was : {number_to_guess}")
                        found = True
                    #If the User finds it in more than 15 attempts
                    else:
                        print(f"Wow, seriousy ? {user_attempt} attempts ? You suck bro\nThe right answer was : {number_to_guess}")
                        found = True
            #If the User makes too many wrong attempts
            else:
                print(f"HOW IS THAT EVEN POSSIBLE LIKE SEIOUSLY ? YOU NEED MORE THAN 30 ATTEMPTS BRO ? No no no I can't accept that, goodbye maybe next time you'll be better.\nThe right answer was {number_to_guess}")
                found = True
    elif int(level) > 1 and int(level) < 4:
        #Upgrade the list to 1000 numbers
        numbers = list(range(1,1000))
        #Pick a new number to find
        number_to_guess = random.choice(numbers)
        #Level 2
        if int(level) == 2:
            #Making an input so User can pick a number
            user_choice = input("Ok so, guess my number...")
            #A While loop that continue as long as the User don't find the answer
            while found == False:
                if user_attempt <= 30 :
                    #Tell the user to choose a number only between 1 and 100
                    if int(user_choice) > 1000 or int(user_choice) < 1:
                        user_choice = input('Hey there, I said between 1 and 100 ! Try again and give me something in that range ;)\n')
                        user_attempt += 1
                    #Tell the User that he picked a number superior as the answer
                    elif int(user_choice) > number_to_guess:
                        user_choice = input('Nice try but... TOO BIGGG\nTry againnn\n')
                        user_attempt += 1
                    #Tell the User that he picked a number inferior as the answer
                    elif int(user_choice) < number_to_guess:
                        user_choice = input("Ouch... TOO TINYYYYY\nMaybe this time you'll be better !\n")
                        user_attempt += 1
                    else:
                        #If the User finds it in one shot
                        if user_attempt == 0:
                            print(f"HOLY SHIIIIIIIIIT, {user_attempt} ATTEMPTS ??? YOU MUST BE KIDDING ME HOW IS THAT EVEN POSSIBLEEE\nThe right answer was : {number_to_guess}")
                            found = True
                        #If the User finds it in less than 5 attempts
                        elif user_attempt < 5:
                            print(f"GOOD JOB BROOOOOOOOOO, {user_attempt} attempts, really nice job !\nThe right answer was : {number_to_guess}")
                            found = True
                        #If the User finds it in less than 15 attempts
                        elif user_attempt < 15:
                            print(f"Well done well done, {user_attempt} attempts, I guess that's not too bad lol\nThe right answer was : {number_to_guess}")
                            found = True
                        #If the User finds it in more than 15 attempts
                        else:
                            print(f"Wow, seriousy ? {user_attempt} attempts ? You suck bro\nThe right answer was : {number_to_guess}")
                            found = True
                #If the User makes too many wrong attempts
                else:
                    print(f"HOW IS THAT EVEN POSSIBLE LIKE SEIOUSLY ? YOU NEED MORE THAN 30 ATTEMPTS BRO ? No no no I can't accept that, goodbye maybe next time you'll be better.\nThe right answer was {number_to_guess}")
                    found = True
        #Level 3
        elif int(level) == 3:
            #Making an input so User can pick a number
            user_choice = input("Ok so, guess my number...")
            #A While loop that continue as long as the User don't find the answer
            while found == False:
                if user_attempt <= 30 :
                    #Tell the user to choose a number only between 1 and 100
                    if int(user_choice) > 1000 or int(user_choice) < 1:
                        user_choice = input('Hey there, I said between 1 and 1000 ! Try again and give me something in that range ;)\n')
                        user_attempt += 1
                    #Tell the User that he picked a number superior as the answer
                    elif int(user_choice) > number_to_guess or int(user_choice) < number_to_guess:
                        user_choice = input('NOPPPPPPP\nTry againnn\n')
                        user_attempt += 1
                    else:
                        #If the User finds it in one shot
                        if user_attempt == 0:
                            print(f"HOLY SHIIIIIIIIIT, {user_attempt} ATTEMPTS ??? YOU MUST BE KIDDING ME HOW IS THAT EVEN POSSIBLEEE\nThe right answer was : {number_to_guess}")
                            found = True
                        #If the User finds it in less than 5 attempts
                        elif user_attempt < 5:
                            print(f"GOOD JOB BROOOOOOOOOO, {user_attempt} attempts, really nice job !\nThe right answer was : {number_to_guess}")
                            found = True
                        #If the User finds it in less than 15 attempts
                        elif user_attempt < 15:
                            print(f"Well done well done, {user_attempt} attempts, I guess that's not too bad lol\nThe right answer was : {number_to_guess}")
                            found = True
                        #If the User finds it in more than 15 attempts
                else:
                    print(f"Wow, seriousy ? {user_attempt} attempts ? You suck bro\nThe right answer was : {number_to_guess}")
                    found = True
            #If the User makes too many wrong attempts
            else:
                print(f"HOW IS THAT EVEN POSSIBLE LIKE SEIOUSLY ? YOU NEED MORE THAN 30 ATTEMPTS BRO ? No no no I can't accept that, goodbye maybe next time you'll be better.\nThe right answer was {number_to_guess}")
                found = True
    #Level 4
    else:
        #Upgrade the list to 1.000.000 numbers
        numbers = list(range(1,1000000))
        #Pick a new number to find
        number_to_guess = random.choice(numbers)
        #Make an input so the User can pick a number
        user_choice = input("Ok, now, one chance, ONLY ONE, you'll not be able to try again, so, guess wich number I've picked between ONE and ONE MILLION\n")
        #A While loop that continue as long as the User don't find the answer
        while found == False:
            #If the user pick a number out of the range it asks a new one
            if int(user_choice) > 1000000 or int(user_choice) < 1:
                user_choice = input("BROOOOO, I SAID BETWEEN 1 AND 1000000 WDYM ?\n")
            elif int(user_choice) == number_to_guess:
                print(f"What ? WHAT ? WDYM YOU FIND IT FIRST SHOT ONE TRY ? HOW IS THAT POSSIBLE LIKE, WHATTTT ? Nah bro you're too good for me, good job.\nThe number to guess was : {number_to_guess}")
                found = True
            else:
                print("Nahh it's ok mannn, like, you had ONE chance in A MILLION how could you had find it ? Nice try bro.")
                found = True

guess_number()