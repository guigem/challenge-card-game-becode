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
        
        '''random pick of cards
        ran = random.choice(self.cards)
        self.history.append(ran)
        print("{} at turn {} played : {} ".format(self.names, self.turns, ran))
        
        return ran '''
        
        print("This is your hand of cards : {}".format(self.cards))
        choice = input("Please pick a number for your card (1 for the first one, 2 for the second, etc.)")
        choice = int(choice)
        self.history.append(self.cards[choice-1])
        print("{} at turn {} played : {} ".format(self.names, self.turns, self.cards[choice-1]))
        
        return self.cards[choice-1]


