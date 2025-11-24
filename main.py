from utils import clear_console
from modules import board, printers

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
    player_move = input("Please enter your move: ")