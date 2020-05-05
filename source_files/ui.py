# ui.py
# @author: Ash Yveth Cudiamat
import blackjack
from player_blackjack import PlayerStates
from player_blackjack import PlayerBlackJack
import card_dealer

class UI:

    def __init__(self):
        self.bljk = blackjack.BlackJack()

    def intro(self):
        print("Welcome to Simple Blackjack")

        # Add 1 player to player list
        x = input("Enter your player name: ")
        self.bljk.add_player(x)

    def play_game(self):

        winner = ''
        while winner == '':
            self.bljk.new_round()
            self.play_round()

            p = input("Play another round? (y/n)")
            if p == 'y':
                winner = ''
            elif p == 'n':
                # Decide winner
                if self.bljk.dealer_wins > self.bljk.players_rounds_won[0]:
                    print("Dealer wins the game.")
                    winner = 'Dealer'
                else:
                    print("You win the game.")
                    winner = "Player"
            else:
                print("Invalid input. Playing another round Anyway.")
        print("Goodbye.")

    def play_round(self):
        print("")
        self.bljk.deal_init_round_cards()

        # Expose one of dealer's cards and show player's deck
        print("Dealer has a " + str(self.bljk.dealer.deck[0].title) +
              " and another card. It's your turn currently.")

        stay = False
        while (stay == False) and (self.bljk.players[0].state == PlayerStates[0]):
            self.bljk.show_player_deck(self.bljk.players[0])
            print("Hit(1) or Stay(0)?")
            x = ''
            while True:
                x = input()
                if x == '1' or x == '0':
                    break
                else:
                    print("Invalid input. Choose hit(1) or stay(0).")
                    
            if x == '1':
                self.bljk.input_turn(self.bljk.players[0], True)
            else:
                stay = True
            print("")

        # Check if player is still alive, dealer gets point if player is dead
        if(self.bljk.players[0].state == PlayerStates[1]):
            self.bljk.show_player_deck(self.bljk.players[0])
            print("You've died.")
            self.bljk.show_dealer_deck()
            print("Dealer wins this Round.")
            self.bljk.increment_dealer_rounds_won()
            return

        print("Now it's the Dealer's Turn")
        while True:
            if (self.bljk.dealer_turn() == False):
                break
        # Check if the dealer died
        if self.bljk.dealer.state == PlayerStates[1]:
            print("The dealer has died an untimely death.")
            self.bljk.show_dealer_deck()
            print("You win this Round.")
            self.bljk.increment_rounds_won(0)
            return
        

        # Provided no one dies...
        print("That ends the round.")

        self.bljk.show_dealer_deck()
        # Both alive. One with higher score wins
        if self.bljk.dealer.score == self.bljk.players[0].score:
            print("Tie.")
        elif(self.bljk.dealer.score > self.bljk.players[0].score):
            print("Dealer wins this round.")
            self.bljk.increment_dealer_rounds_won
        else:
            print("Player wins this round.")
            self.bljk.increment_rounds_won(0)
        return


if __name__ == '__main__':
    # Run the following if running this
    game = UI()
    game.intro()
    game.play_game()
