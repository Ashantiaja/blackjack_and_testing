# player_blackjack.py
# @author Ash Yveth Cudiamat
import cards

PlayerStates = ('alive', 'dead')

class PlayerBlackJack:
    def __init__(self, name = ''):
        if not isinstance(name, str):
            name = ''
        self.deck = []
        self.score = 0
        self.key = name
        self.state = PlayerStates[0]

    def add_card(self, c:cards.Card):
        ''' adds given valid card to this player's deck'''
        if isinstance(c, cards.Card):
            if(c.valid_card):
                self.deck.append(c)
                self.calc_score()
                return True

        return False

    def calc_score(self):
        ''' Recalculates score which this func returns and stores'''
        self.score = 0
        for i in range(0, len(self.deck)):
            self.score += self.deck[i].score
            print(self.score)
        return self.score
                       
    def clear_deck(self):
        ''' Removes all cards from deck '''
        self.deck.clear()

    def show_deck(self):
        ''' Prints deck contents to console '''
        for i in range(0,len(self.deck)):
            print(self.deck[i].title)
