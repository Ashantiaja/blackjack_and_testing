# cards.py
# @author: Ash Yveth Cudiamat

# Dictionaries of cards. wild.
hearts = {
    1: "Ace of Hearts",
    2: "Two of Hearts",
    3: "Three of Hearts",
    4: "Four of Hearts",
    5: "Five of Hearts",
    6: "Six of Hearts",
    7: "Seven of Hearts",
    8: "Eight of Hearts",
    9: "Nine of Hearts",
    10: "Ten of Hearts",
    11: "Jack of Hearts",
    12: "Queen of Hearts",
    13: "King of Hearts"
}

spades = {
    1: "Ace of Spades",
    2: "Two of Spades",
    3: "Three of Spades",
    4: "Four of Spades",
    5: "Five of Spades",
    6: "Six of Spades",
    7: "Seven of Spades",
    8: "Eight of Spades",
    9: "Nine of Spades",
    10: "Ten of Spades",
    11: "Jack of Spades",
    12: "Queen of Spades",
    13: "King of Spades"
}
    
clubs = {
    1: "Ace of Clubs",
    2: "Two of Clubs",
    3: "Three of Clubs",
    4: "Four of Clubs",
    5: "Five of Clubs",
    6: "Six of Clubs",
    7: "Seven of Clubs",
    8: "Eight of Clubs",
    9: "Nine of Clubs",
    10: "Ten of Clubs",
    11: "Jack of Clubs",
    12: "Queen of Clubs",
    13: "King of Clubs"
}

diamonds = {
    1: "Ace of Diamonds",
    2: "Two of Diamonds",
    3: "Three of Diamonds",
    4: "Four of Diamonds",
    5: "Five of Diamonds",
    6: "Six of Diamonds",
    7: "Seven of Diamonds",
    8: "Eight of Diamonds",
    9: "Nine of Diamonds",
    10: "Ten of Diamonds",
    11: "Jack of Diamonds",
    12: "Queen of Diamonds",
    13: "King of Diamonds"
}

suit = {
    1: "Hearts",
    2: "Spades",
    3: "Clubs",
    4: "Diamonds"
}

card_number = {
    1: "Ace of ",
    2: "Two of ",
    3: "Three of ",
    4: "Four of ",
    5: "Five of ",
    6: "Six of ",
    7: "Seven of ",
    8: "Eight of ",
    9: "Nine of ",
    10: "Ten of ",
    11: "Jack of ",
    12: "Queen of ",
    13: "King of "
}

class Card:
    def __init__(self, s = 0, n = 0, su = 0):

        # Score 1-11, invalid is set to 0
        # Num = 1-13, 0 if card is invalid

        self.valid_card = True

        # Score Valid? 1-11 valid
        if s > 11 or s < 1:
            s = 0

        # Suit Valid? 1-4 valid
        if su > 4 or su < 1:
            su = 0
            self.valid_card = False

        # Number Card Valid? 1-13 valid
        if n > 13 or n < 1:
            n = 0
            self.valid_card = False

        self.score = s
        self.suit = su
        self.num = n
        self.title = ''

        if self.valid_card:
            # Calculate title
            self.title = card_number[self.num] + suit[self.suit]

        
        
        
