from utils import clear_console
from modules import board, printers, game_logic

import time

from typing import Tuple, List

#clear_console()
#game_type = input(f"Press 'Enter' to begin: ")

num_moves = 0

current_board = board.Board()

while True:
    num_moves += 1

    clear_console(duration=0.25)

    printers.print_foundation_and_stock(current_board)
    printers.print_card_columns(current_board)

    print("\n\nEnter what column you want to move followed by where you want that card to go. ")
    print("i.e. '5 a' to move the top card of column 5 onto column a")


    player_move : tuple[bool, (str | List[str])] = game_logic.sanatize_user_choice(str(input("\nPlease enter your move: ")))
    while not player_move[0]:
        print(player_move[1])

        clear_console(duration=2.0)
        printers.print_foundation_and_stock(current_board, flush_stock=False)
        printers.print_card_columns(current_board)
        player_move : Tuple[bool, (str | List[str])] = game_logic.sanatize_user_choice(str(input("\n\nPlease enter your move: ")))

    game_logic.move_cards(list(player_move[1]), current_board)

    freeze = input()