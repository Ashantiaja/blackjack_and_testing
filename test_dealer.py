# test_dealer.py
# @author : Ash Yveth Cudiamat

import unittest
from card_dealer import CardDealer
from cards import Card
from random import randrange


class TestDealer(unittest.TestCase):
    def setUp(self):
        self.tDealer = CardDealer()
        
    def tearDown(self):
        self.tDealer.remove_all_cards_in_play()

    def test_remove_cards_in_play(self):
        # 1 card from each suit is set into play
        self.tDealer.hearts_in_play[randrange(0,13)] = True
        self.tDealer.spades_in_play[randrange(0,13)] = True
        self.tDealer.clubs_in_play[randrange(0,13)] = True
        self.tDealer.diamonds_in_play[randrange(0,13)] = True
        self.tDealer.remove_all_cards_in_play()

        # Check all cards to make sure they're no longer
        # in play
        for i in range (0, 13):
            self.assertFalse(self.tDealer.hearts_in_play[i])
            self.assertFalse(self.tDealer.spades_in_play[i])
            self.assertFalse(self.tDealer.clubs_in_play[i])
            self.assertFalse(self.tDealer.diamonds_in_play[i])

    def test_set_valid_card_into_play(self):

        testCard = Card(1,1,1) # Ace of Hearts, score 1
        self.assertTrue(self.tDealer.set_card_in_play(testCard))
        self.assertTrue(self.tDealer.hearts_in_play[0])

        aCard = Card(5, 5, 4) # Five of Diamonds
        self.assertTrue(self.tDealer.set_card_in_play(aCard))
        self.assertTrue(self.tDealer.diamonds_in_play[4])

    def test_set_invalid_card_into_play(self):
        testCard = Card(0,0,0) # Invalid card
        self.assertFalse(self.tDealer.set_card_in_play(testCard))

    def test_remove_valid_card_from_play(self):
        fiveOfSpades = Card(1,5,2)
        self.tDealer.spades_in_play[4] = True # Five of Spades
        self.assertTrue(self.tDealer.remove_card_from_play(fiveOfSpades))
        self.assertFalse(self.tDealer.spades_in_play[4])

    def test_remove_invalid_card_from_play(self):
        # Card isn't in play already
        self.assertFalse(self.tDealer.remove_card_from_play(Card(1,1,1)))

        # Card input isn't valid
        self.assertFalse(self.tDealer.remove_card_from_play(Card(0,0,0)))

    def test_valid_card_num_and_suit(self):
        i = 0
        while i <= 10: # 10 is arbitrary
            pair = self.tDealer.gen_card_values()
            self.assertGreaterEqual(pair[0],1)
            self.assertLessEqual(pair[0],13)
            self.assertGreaterEqual(pair[1],1)
            self.assertLessEqual(pair[1],5)
            i += 1

    def test_in_use_functionality(self):
        playCard = Card(1,10,4) # Ten of Diamonds
        unusedCard = Card(1,3,2) # Three of Spades
        self.tDealer.set_card_in_play(playCard)

        '''self.assertTrue(self.tDealer.in_use(playCard.num,playCard.suit))
        self.assertFalse(self.tDealer.in_use(unusedCard.num,unusedCard.suit))'''
        self.assertTrue(self.tDealer.in_use(playCard))
        self.assertFalse(self.tDealer.in_use(unusedCard))

    def test_dealt_cards_are_valid(self):
        myDeck = list()
        myDeck.append(self.tDealer.deal_card())
        myDeck.append(self.tDealer.deal_card())
        myDeck.append(self.tDealer.deal_card())

        for i in range(0,len(myDeck)):
            self.assertTrue(myDeck[i].valid_card)
            #print(myDeck[i].title)
        #self.tDealer.show_cards_in_play()
    

if __name__ == '__main__':
    unittest.main()
