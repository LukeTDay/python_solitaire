from typing import List

class CardColumn:
    def __init__(self, cards: List[str] | None = None) -> None:
        if cards is None:
            cards = []
        self.cards = cards
        return

    def get_card(self, index=0) -> str:
        if index >= len(self.cards):
            return "  "
        return self.cards[index]
    
    def deal_cards(self, index=0) -> str:
        if len(self.cards) == 0:
            return "|__|"

        if index >= len(self.cards):
            return "  "
        
        if index != 0:
            return "--"
        return self.cards[index]

    def get_all_cards(self) -> List[str]:
        return self.cards
    
    def get_top_card(self) -> str:
        if len(self.cards) == 0:
            return "|__|"
        return self.cards[0]
    
    def remove_card(self,index=0) -> None:
        self.cards.pop(index)
        return
    
    def add_card(self, card : str, index=0) -> None:
        self.cards.insert(index,card)
        return