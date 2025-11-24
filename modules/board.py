from modules.deck import Deck
from modules.cardcolumn import CardColumn
from modules.stock import Stock

from typing import List

class Board:
    def __init__(self) -> None:
        self.deck: Deck = Deck()
        self.column_list : List[CardColumn] = self.generate_rows()
        self.foundations : List[CardColumn] = [CardColumn(),CardColumn(),CardColumn(),CardColumn()]
        self.stock : Stock = self.fill_stock()

    def generate_rows(self) -> List[CardColumn]:
        card_column_list: List[CardColumn] = []
        for x in range(7):
            card_column = CardColumn(self.deck.deal(x+1))
            card_column_list.append(card_column)
        return card_column_list
    
    def fill_stock(self) -> Stock:
        filled_stock = Stock(self.deck.deal(24))
        return filled_stock
    
    def get_column(self, column_id) -> CardColumn | Stock:
        match column_id:
            case '1':
                return self.column_list[0]
            case '2':
                return self.column_list[1]
            case '3':
                return self.column_list[2]
            case '4':
                return self.column_list[3]
            case '5':
                return self.column_list[4]
            case '6':
                return self.column_list[5]
            case '7':
                return self.column_list[6]
            case 'a':
                return self.foundations[0]
            case 'b':
                return self.foundations[1]
            case 'c':
                return self.foundations[2]
            case 'd':
                return self.foundations[3]
            case 'e':
                return self.stock
            case 'f':
                return self.stock
            case 'g':
                return self.stock
        raise IndexError(f"Tried to get the column {column_id}. Does not exist.")

