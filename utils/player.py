from card import Card
import random


class Player:
    
    def __init__(self, list_names, list_cards, num_turns):
        
        '''
        This class is used for players to choose a card. 
        Either randomly or a given chose 
        
        We define:
            - the name of the player (string)
            - its cards (list)
            - the turn they are at (int)
            - the history of cards played (list)
        
        '''
        self.names = list_names
        self.cards = list_cards
        self.turns = num_turns
        self.history = []

    def __str__(self):
        
        return f" list of names : {self.names}, list of cards : {self.cards}, turns : {self.turns}"
        
        
    def play(self):
        
        #Random pick of cards
        '''
        ran = random.choice(self.cards)
        self.history.append(ran)
        print("{} at turn {} played : {} ".format(self.names, self.turns, ran))
        
        return ran '''
        
        #asking for which card the players want to play
        print("This is your hand of cards : {}".format(self.cards))
        choice = input("Please pick a number for your card (1 for the first one, 2 for the second, etc.)")
        choice = int(choice)
        
        
        #adding the given card in the history of the player
        self.history.append(self.cards[choice-1])
        print("{} at turn {} played : {} ".format(self.names, self.turns, self.cards[choice-1]))
        
        
        #returning this card
        return self.cards[choice-1]


