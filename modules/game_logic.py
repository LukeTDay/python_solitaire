from typing import Tuple


def sanatize_user_choice(user_choice : str) -> Tuple[bool,str]:
    user_choice_list = user_choice.strip().split()
    valid_choices = ['1','2','3','4','5','6','7','a','b','c','d','e','f','g']

    print()
    #Checking to make sure the right number of terms are there, should be 2
    if len(user_choice_list) > 2:
        return (False, f"Your choice was invalid\n{user_choice} contains more than two arguments")
    elif len(user_choice_list) < 2:
        return (False, f"Your choice was invalid\n{user_choice} contains less than two arguments")
    
    #Checking to make sure the chosen column actually exists
    if user_choice_list[0] not in valid_choices:
        return (False, f"Your choice was invalid\nThe first argument {user_choice_list[0]} is not a valid column")
    elif user_choice_list[1] not in valid_choices:
        return (False, f"Your choice was invalid\nThe first argument {user_choice_list[1]} is not a valid column")
    
    if user_choice_list[1] in ['e','f','g']:
        return (False, f"Your choice was invalid\nCannot deposit a number into the stock")
    
    #Checking for duplicates
    if user_choice_list[0] == user_choice_list[1]:
        return (False, f"Your choice was invalid\nArguments must be unique")



    return (True, "Correct")