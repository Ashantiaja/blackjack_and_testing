# card_dealer.py
# @author: Ash Yveth Cudiamat

from cards import Card
from random import randrange


class CardDealer:

    # hearts[1] = hearts_in_play[0]
    hearts_in_play = [False, False, False, False,
                      False, False, False, False,
                      False, False, False, False,
                      False]

    spades_in_play = [False, False, False, False,
                      False, False, False, False,
                      False, False, False, False,
                      False]

    clubs_in_play = [False, False, False, False,
                      False, False, False, False,
                      False, False, False, False,
                      False]

    diamonds_in_play = [False, False, False, False,
                      False, False, False, False,
                      False, False, False, False,
                      False]
    
    def __init__(self):
        pass

    def gen_card_values(self):
        ''' returns a tuple representing a random card (unchangeable) (cardNumber, suit)'''
        return (randrange(1,14), randrange(1,5))

    def in_use(self, num, suit):
        ''' returns true if the card is in play already
            returns false if card is invalid or not in use'''
        if(num > 13) or (num < 1):
            return False

        if(suit == 1):
            if(hearts_in_play[num] == True):
                return True
        elif (suit == 2):
            if(spades_in_play[num] == True):
                return True
        elif (suit == 3):
            if(clubs_in_play[num] == True):
                return True
        elif (suit == 4):
            if(diamonds_in_play[num] == True):
                return True

        return False
            

    def deal_card(self):
        ''' returns a Card'''

        # Generate card not in current use                
        cNum = randrange(1,14)
        suit = randrange(1,5)

        score = cNum
        if cNum > 10:
            score = 10

        card = Card(score, cNum, suit)
        if(card.suit == 1):
            pass

    def set_card_in_play(self,c):
        ''' sets the given card's place in the in_play list as True'''
        if(c.valid_card):
            if(c.suit == 1):
                self.hearts_in_play[c.num - 1] = True
                return True
            elif c.suit == 2:
                self.spades_in_play[c.num-1] = True
                return True
            elif c.suit == 3:
                self.clubs_in_play[c.num-1] = True
                return True
            elif c.suit == 4:
                self.diamonds_in_play[c.num-1] = True
                return True
        return False




