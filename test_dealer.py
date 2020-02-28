import unittest
from card_dealer import CardDealer
from cards import Card


class TestDealer(unittest.TestCase):
    def setUp(self):
        #self.tDealer = CardDealer()
        pass
        
    def tearDown(self):
        pass

    def test_set_valid_card_into_play(self):
        tDealer = CardDealer()

        testCard = Card(1,1,1) # Ace of Hearts, score 1
        self.assertTrue(tDealer.set_card_in_play(testCard))
        self.assertTrue(tDealer.hearts_in_play[0])

        aCard = Card(5, 5, 4) # Five of Diamonds
        self.assertTrue(tDealer.set_card_in_play(aCard))
        self.assertTrue(tDealer.diamonds_in_play[4])

    # CURRENT WIP
    # TESTING & adding CARD DEALER FUNCTIONALITY
    def test_generate_unused_cards(self):
        pass
    

if __name__ == '__main__':
    unittest.main()
