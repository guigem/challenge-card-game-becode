from card import Card
from player import Player


class Board:
     
    '''
    This class is there to set the rules of the game and decide what is 
    going to happen. 
    First, all players receive their desks.
    Secondly, they must play one card at each turn.
    Finally, the game ends when no one has cards left
    
    '''
    def __init__(self):
        
        '''
        We define:
            -  list of players (list)
            - the turn we are at (int)
            - a list of all cards present at one turn (list)
            - a dictionnary displaying what card has been played and when (dictionnary)
        
        '''
        
        
        self.obj = Card()
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = {}
        
        
        
    def start_game(self,num_players):
        
          
        '''
        Game process:
            
            - First, distribute cards to each player
            - Secondly, each player plays a card per turn until decks are empty
        '''
        
        #dictionnary to have a track of the name and cards of players
        dicti = {}
        self.num_players = num_players
        
        #Distribution
        distribute = Card.distribute
        distri = distribute(self.obj, self.num_players) 
        
        #Filling dictionnary with name entered and cards distributed
        for i in range(self.num_players):
            log = input("Insert Your name")
            self.players.append(log)
            dicti[i] = {'name' : log, 'cards' : distri[i]}
            print(distri[i])
            
        #create points record
        points = []
        for k in range(num_players):
            points.append(0)        
        
        #Game begins and round starts
        while dicti[0]["cards"]:
            self.turn_count += 1
            
            # each player play one card
            for j in range(len(self.players)):
                
                #Call function in player.py
                p1 = Player(dicti[j]['name'], dicti[j]['cards'],self.turn_count)
                ca = p1.play()
                
                #Add to active cards
                self.active_cards.append(ca)
                
                #remove the played card
                dicti[j]['cards'].remove(ca)
                
            #update history with all cards from a turn
            self.history_cards[self.turn_count] = {"card_played" : self.active_cards}
            

                
                
            
            #messages to let people know the progress of the game
            print("This is the end of turn {}".format(self.turn_count)) 
            print("The cards played this turn are {}".format(self.active_cards))
            print("List of cards already played in the game : {}".format(self.history_cards))
            
            #reset a new active list
            self.active_cards = []
        
        #Last message when the game is done
        return "Game is over"   
            


t = ["K", "9", "8"]
if "K" in t:
    t.index("K")
