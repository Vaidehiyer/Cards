"""The cards module contains classes for representing playing cards and decks of cards.

The module contains two classes:
- Card: represents a single playing card with a value and suit
- Deck: represents a deck of playing cards, which can be shuffled and drawn from
"""


class Card:
    """
    A class representing a single playing card.

    Attributes:
        value (int): the numeric value of the card (2-10 for numbered cards, 11-14 for face cards)
        suit (str): the suit of the card (Clubs, Diamonds, Hearts, Spades)
        name_dict (dict): a dictionary mapping face card values to their names (11: Jack, 12: Queen, 13: King, 14: Ace)

    Methods:
        __init__(self, value, suit): creates a new Card object with the given value and suit
        __str__(self): returns a string representation of the card (e.g. "10 of Hearts")

    """

    name_dict = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, value, suit):
        """
        Creates a new Card object with the given value and suit.

        Args:
            value (int): the numeric value of the card (2-10 for numbered cards, 11-14 for face cards)
            suit (str): the suit of the card (Clubs, Diamonds, Hearts, Spades)

        Raises:
            ValueError: if the value is not in the valid range (2-14)

        """
        self.suit = suit
        self.value = value
        if 2 <= self.value <= 10:
            self.name = str(self.value)
        elif self.value in self.name_dict:
            self.name = self.name_dict[self.value]
        else:
            raise ValueError("Invalid card value")

    def __str__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: a string representation of the card (e.g. "10 of Hearts")

        """
        return "{} of {}".format(self.name, self.suit)
