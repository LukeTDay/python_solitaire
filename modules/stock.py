from typing import List

class Stock:

    def __init__(self, cards : List[str]) -> None:
        self.cards = cards
        self.index = 0
        return
    
    def get_next_three_cards(self, num = 3) -> List[str]:
        cards = []
        cards_left = len(self.cards)
        for iterator in range(0,num):
            if (self.index + iterator) >= cards_left:
                cards.append("|__|")
            else:
                cards.append(self.cards[self.index+iterator])
        if (self.index + (num-1)) >= cards_left:
            self.index = 0
        else:
            self.index = self.index + (num-1)

        return cards