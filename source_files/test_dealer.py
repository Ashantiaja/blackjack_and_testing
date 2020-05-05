# test_dealer.py
# @author : Ash Yveth Cudiamat

import pytest
from card_dealer import CardDealer
from cards import Card
from random import randrange


class TestDealer:

    @classmethod
    def setup_class(self):
        self.tDealer = CardDealer()

    @classmethod
    def teardown_class(self):
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
            #self.assertFalse(self.tDealer.hearts_in_play[i])
            assert self.tDealer.hearts_in_play[i] == False
            #self.assertFalse(self.tDealer.spades_in_play[i])
            assert self.tDealer.spades_in_play[i] == False
            #self.assertFalse(self.tDealer.clubs_in_play[i])
            assert self.tDealer.clubs_in_play[i] == False
            #self.assertFalse(self.tDealer.diamonds_in_play[i])
            assert self.tDealer.diamonds_in_play[i] == False

    def test_set_valid_card_into_play(self):

        testCard = Card(1,1,1) # Ace of Hearts, score 1
        #self.assertTrue(self.tDealer.set_card_in_play(testCard))
        #self.assertTrue(self.tDealer.hearts_in_play[0])
        assert self.tDealer.set_card_in_play(testCard) == True
        assert self.tDealer.hearts_in_play[0] == True

        aCard = Card(5, 5, 4) # Five of Diamonds
        #self.assertTrue(self.tDealer.set_card_in_play(aCard))
        #self.assertTrue(self.tDealer.diamonds_in_play[4])
        assert self.tDealer.set_card_in_play(aCard) == True
        assert self.tDealer.diamonds_in_play[4] == True

    def test_set_invalid_card_into_play(self):
        testCard = Card(0,0,0) # Invalid card
        #self.assertFalse(self.tDealer.set_card_in_play(testCard))
        assert self.tDealer.set_card_in_play(testCard) == False

    def test_remove_valid_card_from_play(self):
        fiveOfSpades = Card(1,5,2)
        self.tDealer.spades_in_play[4] = True # Five of Spades
        #self.assertTrue(self.tDealer.remove_card_from_play(fiveOfSpades))
        #self.assertFalse(self.tDealer.spades_in_play[4])
        assert self.tDealer.remove_card_from_play(fiveOfSpades) == True
        assert self.tDealer.spades_in_play[4] == False

    def test_remove_invalid_card_from_play(self):
        self.tDealer.remove_all_cards_in_play()
        # Card isn't in play already
        #self.assertFalse(self.tDealer.remove_card_from_play(Card(1,1,1)))
        assert self.tDealer.remove_card_from_play(Card(1,1,1)) == False

        # Card input isn't valid
        #self.assertFalse(self.tDealer.remove_card_from_play(Card(0,0,0)))
        assert self.tDealer.remove_card_from_play(Card(0,0,0)) == False

    def test_valid_card_num_and_suit(self):
        i = 0
        while i <= 10: # 10 is arbitrary
            pair = self.tDealer.gen_card_values()
            #self.assertGreaterEqual(pair[0],1)
            assert pair[0] >= 1
            #self.assertLessEqual(pair[0],13)
            assert pair[0] <= 13
            # self.assertGreaterEqual(pair[1],1)
            assert pair[1] >= 1
            #self.assertLessEqual(pair[1],5)
            assert pair[1] <= 5
            i += 1

    def test_in_use_functionality(self):
        playCard = Card(1,10,4) # Ten of Diamonds
        unusedCard = Card(1,3,2) # Three of Spades
        self.tDealer.set_card_in_play(playCard)

        '''self.assertTrue(self.tDealer.in_use(playCard.num,playCard.suit))
        self.assertFalse(self.tDealer.in_use(unusedCard.num,unusedCard.suit))'''
        #self.assertTrue(self.tDealer.in_use(playCard))
        #self.assertFalse(self.tDealer.in_use(unusedCard))
        assert self.tDealer.in_use(playCard) == True
        assert self.tDealer.in_use(unusedCard) == False

    def test_dealt_cards_are_valid(self):
        myDeck = list()
        myDeck.append(self.tDealer.deal_card())
        myDeck.append(self.tDealer.deal_card())
        myDeck.append(self.tDealer.deal_card())

        for i in range(0,len(myDeck)):
            #self.assertTrue(myDeck[i].valid_card)
            assert myDeck[i].valid_card == True
