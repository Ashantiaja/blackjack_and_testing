import pytest
from cards import Card

class TestCards:

    @classmethod
    def setup_class(self):
        self.validCard = Card(1,1,1)

    def test_invalid_score(self):
        t = Card(58, 1,1)
        # self.assertEqual(t.score, 0)
        assert t.score == 0

        t = Card(-5, 1,1)
        #self.assertEqual(t.score, 0)
        assert t.score == 0

    def test_invalid_num(self):
        t = Card(1, 14,1)
        assert t.num == 0

        t = Card(1, -1,1)
        assert t.num == 0

    def test_invalid_suit(self):
        t = Card(1, 1, 15)
        assert t.suit == 0

        t = Card(1, 1, -1000)
        assert t.suit == 0

    def test_correct_card_initialization(self):
        t = Card(1, 10, 2) # Ten of Spades
        assert t.title == "Ten of Spades"

    def test_card_knows_if_its_valid(self):
        t = Card()
        assert t.valid_card is False
        assert self.validCard.valid_card == True
        
