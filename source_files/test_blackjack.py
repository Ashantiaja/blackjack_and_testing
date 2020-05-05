# test_dealer.py
# @author : Ash Yveth Cudiamat

import pytest
import blackjack
from cards import Card
from player_blackjack import PlayerBlackJack
from player_blackjack import PlayerStates

class TestBlackJack:
    def setup_class(self):
        self.bljk = blackjack.BlackJack()
        self.randomPlayer = PlayerBlackJack()
        self.randomPlayer.key = 'Random Player'

    def teardown_class(self):
        self.bljk.new_game()

    def test_new_game(self):
        a = PlayerBlackJack("a")
        b = PlayerBlackJack("b")
        defCard = Card(1,1,1)
        a.add_card(defCard)
        b.add_card(defCard)
        self.bljk.dealer.add_card(defCard)
        self.bljk.players.append(a)
        self.bljk.players.append(b)
        self.bljk.new_game()

        assert len(self.bljk.players) == 0
        assert len(self.bljk.dealer.deck) == 0
        assert len(self.bljk.players_rounds_won) == 0
        assert self.bljk.dealer_wins == 0

    def test_new_round(self):
        # Each player should have an empty deck
        a = PlayerBlackJack("a")
        b = PlayerBlackJack("b")
        defCard = Card(1,1,1)
        a.add_card(defCard)
        b.add_card(defCard)
        self.bljk.dealer.add_card(defCard)
        self.bljk.players.append(a)
        self.bljk.players.append(b)
        self.bljk.new_round()

        assert len(self.bljk.players[0].deck) == 0
        assert len(self.bljk.players[1].deck) == 0
        assert len(self.bljk.dealer.deck) == 0
        

    def test_add_player(self):
        # add player func returns true with successful addition
        # also check player list to ensure success
        self.bljk.new_game()
        assert self.bljk.add_player(10) == False
        assert self.bljk.add_player("Danny Devito") == True
        assert self.bljk.players[0].key == "Danny Devito"
        
    def test_generate_init_cards(self):
        # Check that 2 cards are created for each player & dealer
        self.bljk.players.append(self.randomPlayer)
        aPlayer = PlayerBlackJack()
        aPlayer.key = "Another Player"
        self.bljk.players.append(aPlayer)
        self.bljk.deal_init_round_cards()

        assert len(self.bljk.dealer.deck) == 2
        for i in range(0, len(self.bljk.players)):
            assert len(self.bljk.players[i].deck) == 2

    def test_update_player_state(self):
        self.bljk.new_game()
        self.randomPlayer.score = 30
        self.bljk.players.append(self.randomPlayer)
        self.bljk.update_player_state(self.bljk.players[0])

        assert self.bljk.players[0].state == PlayerStates[1]

        self.bljk.dealer.score = 1
        self.bljk.update_player_state(self.bljk.dealer)

        assert self.bljk.dealer.state == PlayerStates[0]

    def test_dead_player_taking_turn(self):
        self.bljk.new_game()
        self.randomPlayer.clear_deck()
        a = Card(10,10,1) # Ten of Hearts
        b = Card(10,10,2) # Ten of Spades
        c = Card(10,10,3) # Ten of Clubs
        self.randomPlayer.add_card(a)
        self.randomPlayer.add_card(b)
        self.randomPlayer.add_card(c)
        self.bljk.players.append(self.randomPlayer)
        self.bljk.update_player_state(self.bljk.players[0])
        self.bljk.input_turn(self.bljk.players[0], True)

        # Despite the hit, player should still only have 3 cards
        assert len(self.bljk.players[0].deck) == 3
        

    def test_player_takes_turn_successfully(self):
        self.bljk.new_game()
        self.randomPlayer = PlayerBlackJack()
        self.bljk.players.append(self.randomPlayer)
        self.bljk.input_turn(self.bljk.players[0], True)

        # One card should be in the player's deck since they hit
        assert len(self.bljk.players[0].deck) == 1
