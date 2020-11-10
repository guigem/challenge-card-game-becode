from card import Card
from player import Player


class Board:
     
    def __init__(self):
        
        self.obj = Card()
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = {}
        
    def start_game(self,num_players):
        
           
        
        dicti = {}
        self.num_players = num_players
        distribute = Card.distribute
        distri = distribute(self.obj, self.num_players) 
        for i in range(self.num_players):
            log = input("Insert Your name")
            self.players.append(log)
            dicti[i] = {'name' : log, 'cards' : distri[i]}
            print(distri[i])
            
        while dicti[0]["cards"]:
            self.turn_count += 1
            for j in range(len(self.players)):
                p1 = Player(dicti[j]['name'], dicti[j]['cards'],self.turn_count)
                ca = p1.play()
                self.active_cards.append(ca)
                dicti[j]['cards'].remove(ca)
            self.history_cards[self.turn_count] = {"card_played" : self.active_cards}
            
            print("This is the end of turn {}".format(self.turn_count)) 
            print("The cards played this turn are {}".format(self.active_cards))
            print("List of cards already played in the game : {}".format(self.history_cards))
            self.active_cards = []
        return "Game is over"   
            
