from card import Card


class Board:
     
    def __init__(self):
        
        self.obj = Card()
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = {}
        
    def start_game(self,num_players):
        
           
        name = []
        dicti = {}
        self.num_players = num_players
        distribute = Card.distribute
        distri = distribute(self.obj, self.num_players) 
        for i in range(self.num_players):
            log = input("Insert Your name")
            name.append(log)
            dicti[i] = {'name' : log, 'cards' : distri[i]}
            print(distri)
        
            
