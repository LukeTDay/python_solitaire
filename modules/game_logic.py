from typing import Tuple, List, cast
from modules.board import Board
from modules.cardcolumn import CardColumn


def sanatize_user_choice(user_choice : str) -> Tuple[bool,(str | List[str])]:
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
    
    return (True, user_choice_list)

def move_cards(user_choice: List[str], board : Board) -> bool:
    column_to_take_from = user_choice[0]
    column_to_move_to = user_choice[1]

    column_locations = ['1','2','3','4','5','6','7']
    foundation_locations = ['a','b','c','d']
    stock_locations = ['e','f','g']

    to_foundation = False
    to_column = False

    column_to_move_to_card = ""
    column_to_take_from_card = ""

    if column_to_take_from in column_locations:
        column_to_take_from_card = board.column_list[int(user_choice[0]) - 1].get_top_card()
    
    if column_to_move_to in column_locations:
        column_to_move_to_card = board.column_list[int(user_choice[1]) - 1].get_top_card()
        to_column = True

    if not can_move_cards(column_to_take_from_card,
                            int(user_choice[0]),
                            int(user_choice[1]),
                            column_to_move_to_card,
                            board,
                            to_foundation=to_foundation,
                            to_column=to_column):
        return False
    
    return True

def can_move_cards(card_to_move : str, move_index : int, stack_index : int, card_to_stack_under : str, board : Board, to_foundation : bool = False, to_column : bool = False) -> bool:
    ordered_list = ['K','Q','J','10','9','8','7','6','5','4','3','2','1']

    card_to_move_split = list(card_to_move)
    move_color = card_to_move_split[0]
    move_suit = card_to_move_split[1]
    move_type = card_to_move_split[2]
    if len(card_to_move_split) > 3:
        move_type = move_type + card_to_move_split[3]

    card_to_stack_under_split = list(card_to_stack_under)
    stack_color = card_to_stack_under_split[0]
    stack_suit = card_to_stack_under_split[1]
    stack_type = card_to_stack_under_split[2] 
    if len(card_to_stack_under_split) > 3:
        stack_type = stack_type + card_to_stack_under_split[3]

    if to_column:
        if stack_type == 'A' or move_type == 'A': 
            return False

        index = ordered_list.index(stack_type)
        if move_color != stack_color and ordered_list[index+1] == move_type:
            #Remove from move
            board.get_column(str(move_index)).remove_card()
            #Add to stack
            cast(CardColumn,board.get_column(str(stack_index))).add_card(card_to_move)
            print("Moved cards")
            
    return True
