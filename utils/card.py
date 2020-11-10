import random

class Symbol:
    
    def __init__(self):
        
        #initialize the colors and the icons
        self.color = ["black", "red"]
        self.icon = ["♥","♦","♣","♠"]
        
class Card(Symbol):
    
    def __init__(self):
        #initialize the rest of the data like the value of cards
        super().__init__()
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        
    def fill_deck(self):
        
        #create all combination of cards with symbols and numbers 
        self.icons = ["♥","♦","♣","♠"]
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
       
        #store them in a list
        cd = []
        for i in self.value:
            for j in self.icons: 
                mix = i + j
                cd.append(mix)
                
        return cd
    
    def shuffle(self):
        
        #shuffle the deck of cards with random function shuffle
        h = Card
        self.deck = Card.fill_deck(h)
        random.shuffle(self.deck)
        
        return self.deck
    
    def distribute(self, number_player):
        
        '''distribute a given number of cards to each player.
        The number of cards given can be computed using:
            number of total cards // number of players
            Everyone should the maximum and same amount of cards
        
        each player's deck is a element in the following list'''
        self.vec = []
        m = Card
        
        #need to know the number of players
        self.numberplayer = number_player
        
        #assign a number of cards depending on the number of players
        for i in range(number_player):
            
            #intermediate list
            self.inter = []
            
            #creating the decks and storing each one of them in a list
            for u in range(52//number_player):  
               
                self.inter.append(Card.shuffle(m)[u])
                
            self.vec.append(self.inter)
            
            for o in self.inter:
                #removing the cards in order to avoid doubles
               Card.shuffle(m).remove(o)
          
        #return the vector with all the decks
        return self.vec
            

            
    


