# test_player.py
# @author Ash Yveth Cudiamat
import pytest
from player_blackjack import PlayerBlackJack
from cards import Card

class TestPlayerBlackJack:

    @classmethod
    def setup_class(self):
        self.player = PlayerBlackJack()

    @classmethod
    def teardown_class(self):
        self.player.clear_deck()
        self.player.score = 0

    def test_add_card_to_deck(self):
        c = Card(5,11,2) # Jack of Spades score 5
        #self.assertTrue(self.player.add_card(c))
        assert self.player.add_card(c) == True
        #self.assertEqual(self.player.deck[0], c)
        assert self.player.deck[0] == c

    def test_add_invalid_input_to_deck(self):
        #self.assertFalse(self.player.add_card(5))
        assert self.player.add_card(5) == False
        c = Card(0,0,0)
        #self.assertFalse(self.player.add_card(c))
        assert self.player.add_card(c) == False

    def test_calc_score_correctly(self):
        self.player.clear_deck()
        a = Card(5,2,2)
        b = Card(10, 10, 1)
        c = Card(1, 3, 3)
        self.player.add_card(a)
        self.player.add_card(b)
        self.player.add_card(c)
        self.player.show_deck()
        #self.assertEqual(self.player.calc_score(), 16)
        assert self.player.calc_score() == 16

    def test_clear_deck(self):
        c = Card(1,1,1) # Ace of Hearts Score 1
        self.player.deck.append(c)
        self.player.clear_deck()
        #self.assertEqual(self.player.deck, [])
        assert self.player.deck == []

