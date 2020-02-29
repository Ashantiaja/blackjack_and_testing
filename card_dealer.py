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
        list_num = num-1
        if(suit == 1):
            if(self.hearts_in_play[list_num] == True):
                return True
        elif (suit == 2):
            if(self.spades_in_play[list_num] == True):
                return True
        elif (suit == 3):
            if(self.clubs_in_play[list_num] == True):
                return True
        elif (suit == 4):
            if(self.diamonds_in_play[list_num] == True):
                return True

        return False

    
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


    def deal_card(self):
        ''' returns a Card'''
        
        # Emulating a do while here
        # Generate card values until an unused one is
        # made
        while True:
            cardVal = self.gen_card_values()
            if not self.in_use(cardVal[0], cardVal[1]):
                break
        score = cardVal[0]
        if cardVal[0] > 10:
            score = 10
        # Create the actual card
        dealCard = Card(score, cardVal[0], cardVal[1])

        # Set card to in-play
        self.set_card_in_play(dealCard)

        # Give the card away
        return dealCard

    def remove_card_from_play(self, num, suit):
        # Valid input
        if (num < 1 or num > 13 or
            suit < 1 or suit > 4):
            return False
        arrayNum = num-1

        if suit == 1:
            if(self.hearts_in_play[arrayNum] == True):
                self.hearts_in_play[arrayNum] = False
                return True
            return False
        elif suit == 2:
            if(self.spades_in_play[arrayNum] == True):
                self.spades_in_play[arrayNum] = False
                return True
            return False
        elif suit == 3:
            if(self.clubs_in_play[arrayNum] == True):
                self.clubs_in_play[arrayNum] = False
                return True
            return False
        elif suit == 4:
            if(self.diamonds_in_play[arrayNum] == True):
                self.diamonds_in_play[arrayNum] = False
                return True
            return False

    def remove_all_cards_in_play(self):
        ''' Sets all in-play cards to false. '''
        for i in range(0,13):
            self.hearts_in_play[i] = False
            self.spades_in_play[i] = False
            self.clubs_in_play[i] = False
            self.diamonds_in_play[i] = False

    def show_cards_in_play(self):
        for i in range(0,13):
            if self.hearts_in_play[i] == True:
                print( str(i+1) + " of Hearts" )
            if self.spades_in_play[i] == True:
                print( str(i+1) + " of Spades" )
            if self.clubs_in_play[i] == True:
                print( str(i+1) + " of Clubs" )
            if self.diamonds_in_play[i] == True:
                print( str(i+1) + " of Diamonds" )


