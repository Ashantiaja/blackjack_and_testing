import unittest
from cards import Card

class TestCards(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #@unittest.skip("Add testing conditions for this later")
    def test_invalid_score(self):
        t = Card(58, 1,1)
        self.assertEqual(t.score, 0)

    def test_invalid_num(self):
        t = Card(1, 14,1)
        self.assertEqual(t.num,0)

    def test_invalid_suit(self):
        t = Card(1, 1, 15)
        self.assertEqual(t.suit, 0)


    def test_correct_card_initialization(self):
        t = Card(1, 10, 2) # Ten of Spades
        self.assertEqual(t.title, "Ten of Spades")
        


if __name__ == '__main__':
    unittest.main()
