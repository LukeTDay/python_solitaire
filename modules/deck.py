from typing import List
import random

class Deck:

    def __init__(self) -> None:
        self.num_cards = self.create_random_deck()
        return
    
    def create_random_deck(self) -> List[str]:
        randomized_list : List[str] = []
        for y in ["S","H","D","C"]:
            if y == "H" or y == "D":
                for x in range(10):
                    randomized_list.append(f"R{y}{x+1}")
                randomized_list.append(f"R{y}J")
                randomized_list.append(f"R{y}Q")
                randomized_list.append(f"R{y}K")
                randomized_list.append(f"R{y}A")
            elif y == "C" or y == "S":
                for x in range(10):
                    randomized_list.append(f"B{y}{x+1}")
                randomized_list.append(f"B{y}J")
                randomized_list.append(f"B{y}Q")
                randomized_list.append(f"B{y}K")
                randomized_list.append(f"B{y}A")

        random.shuffle(randomized_list)

        return randomized_list

    def deal(self, num_to_deal) -> List[str]:
        length_of_deck = len(self.num_cards)
        if num_to_deal > length_of_deck:
            raise IndexError(f"You requested to deal {num_to_deal} cards but there are only {length_of_deck} left in the deck")
        cards_to_deal = self.num_cards[:num_to_deal]
        self.num_cards = self.num_cards[num_to_deal:]
        return cards_to_deal