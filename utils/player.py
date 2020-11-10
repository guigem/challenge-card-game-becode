from card import Card
import random


class Player:
    
    def __init__(self, list_names, list_cards, num_turns):
        
        #obj = Card()
        #self.cards = obj.fill_deck()
        self.names = list_names
        self.cards = list_cards
        self.turns = num_turns
        self.history = []

        
    def play(self):
        
        #for i in self.names:
        ran = random.choice(self.cards)
        self.history.append(ran)
        print("{} at turn {} played : {} ".format(self.names, self.turns, ran))
        
        return ran

        


