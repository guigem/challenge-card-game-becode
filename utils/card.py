import random

class Symbol:
    
    def __init__(self):
        
        self.color = ["black", "red"]
        self.icon = ["♥","♦","♣","♠"]
        
class Card(Symbol):
    
    def __init__(self):
        
        col = Symbol()
        self.colors = col.color
        self.icons = col.icon
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        
    def fill_deck(self):
        
        self.colors = ["black", "red"]
        self.icons = ["♥","♦","♣","♠"]
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        cd = []
        for i in self.value:
            for j in self.icons: 
                mix = i + j
                cd.append(mix)
                
        return cd
    
    def shuffle(self):
        
        h = Card
        self.deck = Card.fill_deck(h)
        random.shuffle(self.deck)
        
        return self.deck
    
    def distribute(self, number_player):
        
        self.vec = []
        h = Card
        self.numberplayer = number_player
        for i in range(number_player):
            
            self.inter = []
            for u in range(6):  
               
                self.inter.append(Card.shuffle(h)[u])
            self.vec.append(self.inter)
            for o in self.inter:
               Card.shuffle(h).remove(o)
                
        return self.vec
            
            
 
            
            

            
    


