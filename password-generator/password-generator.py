#Made by Jean

import random
import string


def generate_passwrd():
    passwrd = ''
    #User make all his choices
    choice_length, choice_majs, choice_numbers, choice_symbols = choice()
    
    #Importing letters, numbers and symbols
    letters_min = string.ascii_lowercase
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    #All combinations of choices
    all_y = letters + numbers + symbols
    digi_symb_y = letters_min + numbers + symbols
    digi_majs_y = letters + numbers
    symb_majs_y = letters + symbols
    symb_y = letters_min + symbols
    digi_y = letters_min + numbers
    majs_y = letters
    
    #Setting the length from string to int
    length = int(choice_length)

    if choice_numbers == 'Y':
        if choice_symbols == 'Y':
            if choice_majs == 'Y':
                #Password will have all the securities allowed
                passwrd = ''.join(random.choices(all_y, k=length))
            else:
                #Password will have number and symbols but no majs
                passwrd = ''.join(random.choices(digi_symb_y, k=length))
        elif choice_majs == 'Y':
            #Password will have majs and numbers but no symbols
            passwrd = ''.join(random.choices(digi_majs_y, k=length))
        else:
            #Password will have numbers but no majs and symbols
            passwrd = ''.join(random.choices(digi_y, k=length))
    elif choice_symbols == 'Y':
        if choice_majs == 'Y':
            #Password will have symbols and majs but no numbers
            passwrd = ''.join(random.choices(symb_majs_y, k=length))
        else:
            #Password will have symbols but no majs and numbers
            passwrd = ''.join(random.choices(symb_y, k=length))
    elif choice_majs == 'Y':
        #Password will have majs but no numbers or symbols
        passwrd = ''.join(random.choices(majs_y, k=length))
    else:
        #Password will have no security excepted some letters, not good :(
        print("You didn't selected any type of character, your password will not be secured !")
        passwrd = ''.join(random.choices(letters_min, k=length))
        
    #Telling password to user
    print('Your password is: ' + passwrd)


def choice():
    #User select if he wanna have numbers in his password
    choice_numbers = input('Do you want your passwrd to have number ? (Y/N)')
    #If user don't select anything, then he will be asked to choose something unless he chosees one to continue
    while choice_numbers not in ['Y', 'N']:
        choice_numbers = input('You need to type Y or N !')
        
    #User select if he wanna have MAJs in his password
    choice_majs = input('Do you want your passwrd to have MAJs ? (Y/N)')
    #If user don't select anything, then he will be asked to choose something unless he chosees one to continue
    while choice_majs not in ['Y', 'N']:
        choice_majs = input('You need to type Y or N !')
        
    #User select if he wanna have symbols in his password
    choice_symbols = input('Do you want your passwrd to got special symbols ? (Y/N)')
    #If user don't select anything, then he will be asked to choose something unless he chosees one to continue
    while choice_symbols not in ['Y', 'N']:
        choice_symbols = input('You need to type Y or N !')
        
    #If user don't type digits to have a length, then he will be asked to type digits unless he types one or nothing to continue
    while True :
        #User chooses the length of his password
        choice_length = input('Which length must be your passwrd ? (Let it empty to stay with default 10 character lentgh)')
        if choice_length == '' :
            #Default password length, choosen if user don't type anything
            choice_length = '10'
            break #To get out of the loop
        elif not choice_length.isdigit() :
            print("Merci d’entrer un nombre valide.")
        else :
         break #To get out of the loop
        
    #Return the choices of the user
    return choice_length, choice_majs, choice_numbers, choice_symbols


generate_passwrd()