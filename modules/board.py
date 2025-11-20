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
