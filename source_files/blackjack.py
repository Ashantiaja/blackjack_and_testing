# blackjack.py
# @author: Ash Yveth Cudiamat

from card_dealer import CardDealer
from random import randrange
import cards
import player_blackjack

class BlackJack:
    threshold = 21
    dealerDeck = CardDealer()
    dealer = player_blackjack.PlayerBlackJack()
    dealer_wins = 0
    players = list()
    players_rounds_won = list()

    def __init__(self):
        self.dealer.key = "Dealer"

    def new_game(self):
        self.players.clear() # Remove all players
        self.players_rounds_won.clear()
        self.dealer.clear_deck()
        self.dealer_wins = 0

    def new_round(self):
        ''' Clears player's decks and sets them to alive again'''
        self.dealer.clear_deck()
        self.update_player_state(self.dealer)

        for i in range(0, len(self.players)):
            self.players[i].clear_deck()
            self.update_player_state(self.players[i])

    def add_player(self, name):
        if not isinstance(name, str):
            return False

        newPlayer = player_blackjack.PlayerBlackJack()
        newPlayer.key = name
        self.players.append(newPlayer)
        self.players_rounds_won.append(0)
        #print("Length of players rounds won: " + str(len(self.players_rounds_won)))
        return True

    def increment_dealer_rounds_won(self):
        self.dealer_wins += 1

    def increment_rounds_won(self, player_index):
        if not isinstance(player_index, int):
            return
        if player_index < 0 or player_index >= len(self.players):
            return

        self.players_rounds_won[player_index] += 1        

    def deal_init_round_cards(self):
        ''' Deals 2 cards to dealer and each player '''
        self.dealer.add_card(self.dealerDeck.deal_card())
        self.dealer.add_card(self.dealerDeck.deal_card())
        self.update_player_state(self.dealer)

        for i in range(0,len(self.players)):
            self.players[i].add_card(self.dealerDeck.deal_card())
            self.players[i].add_card(self.dealerDeck.deal_card())
            self.update_player_state(self.players[i])

    def dealer_turn(self):
        ''' Assuming dealer is still alive, decide to draw or not draw'''
        ''' Return true if card was dealt, return false otherwise'''
        # Check if dealer is dead first
        if self.dealer.state == player_blackjack.PlayerStates[1]:
            return False

        if self.dealer.score <= 10:
            self.dealer.add_card(self.dealerDeck.deal_card())
            return True
        else:
            # Dealer more likely to hit if farther from threshold
            x = randrange(0,12) #0-11
            if (self.dealer.score + x) <= self.threshold:
                # Hit
                self.dealer.add_card(self.dealerDeck.deal_card())
                self.update_player_state(self.dealer)
                return True
            else:
                return False
        return False

    def update_player_state(self,p):
        if not isinstance(p, player_blackjack.PlayerBlackJack):
            return 

        if p.score > self.threshold:
            p.state = player_blackjack.PlayerStates[1] # Dead
        else:
            p.state = player_blackjack.PlayerStates[0] # Alive

    def input_turn(self,p, is_hit):
        ''' Takes in intended player and bool True if hit false if stay'''
        # Check for valid input
        if not isinstance(p, player_blackjack.PlayerBlackJack):
            return
        if not isinstance(is_hit, bool):
            return

        # Check if player is dead
        if p.state == player_blackjack.PlayerStates[1]:
            return

        # Take turn, hit or not.
        if is_hit:
            p.add_card(self.dealerDeck.deal_card())
            self.update_player_state(p)
    

    def show_dealer_deck(self):
        print(self.dealer.key + "'s Deck: ")
        for i in range(0, len(self.dealer.deck)):
            print(self.dealer.deck[i].title)
        print("Score: " + str(self.dealer.score))
        print("Status: " + self.dealer.state)

    def show_player_deck(self, p):
        if not isinstance(p, player_blackjack.PlayerBlackJack):
            return


        print(p.key + "'s Deck: ")
        for j in range(0, len(p.deck)):
            print(p.deck[j].title)
        print("Score: " + str(p.score))
        print("Status: " + p.state)

    def show_player_decks(self):
        for i in range(0, len(self.players)):
            print(self.players[i].key + "'s Deck: ")
            for j in range(0, len(self.players[i].deck)):
                print(self.players[i].deck[j].title)
            print("Score: " + str(self.players[i].score))
            print("Status: " + self.players[i].state)
            
