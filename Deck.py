import random
from Card import Card


class Deck:
    """
    A class representing a deck of playing cards.

    Attributes:
        cards (list): a list of Card objects representing the cards in the deck

    Methods:
        __init__(self): creates a new Deck object with all 52 cards in a random order
        draw(self): removes and returns a Card object from the deck, if there are any left
    """

    def __init__(self):
        """
        Creates a new Deck object with all 52 cards in a random order.
        """
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for value in range(2, 15):
                card = Card(value, suit)
                self.cards.append(card)
        random.shuffle(self.cards)

    def draw(self):
        """
        Removes and returns a Card object from the deck, if there are any left.

        Returns:
            Card: the top card from the deck

        Raises:
            RuntimeError: if the deck is empty

        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise RuntimeError("The deck is empty")
