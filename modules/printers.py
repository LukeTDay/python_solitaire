from modules.board import Board



def print_card_columns(board: Board) -> None:
    #Prints the columns of cards
    max_height = max(len(col.cards) for col in board.column_list)

    print(f"{'Cards':-^40}\n")
    for x in range(max_height,-1,-1):
        for y in range(0,7):
            print(f"{(board.column_list[y]).deal_cards(x):^5}", end=" ")
        print("\n")
    for x in range(0,7):
        print(f"{x+1:^5}", end=" ")
    return None

def print_foundation_and_stock(board: Board) -> None:
    print(f"{'Solitaire':-^40}\n")
    for foundation in board.foundations:
        print(f"{foundation.get_top_card():^5}", end=" ")
    for card in board.stock.get_next_three_cards():
        print(f"{card:^5}", end=" ")
    print("\n")
    for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        print(f"{x:^5}", end=" ")
    print("\n")

    return