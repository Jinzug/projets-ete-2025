#Made by Jean
#Objectives :
#-Pick a number between 1 and 100
#-Make a loop that ends when User found the right number
#-Tell User evidences like "Too big !", "Too tiny !"
#-Let the User choose level of difficulty
#-If User exceed 25 attempts he losts

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

    #Launch input
    user_choice = input('Hi ! Welcome to the Guess Number Game !\nI picked a number between 1 and 100, so tell me, which one ddo you think I picked ?\n')

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


guess_number()