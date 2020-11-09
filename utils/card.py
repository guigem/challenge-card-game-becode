
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
        
        dic = {}
        h = 0
        for i in range(len(self.value)):
            for j in self.icons: 
                
                if j == "♥" or j == "♦":
                    sym = self.colors[1]
                else:
                    sym = self.colors[0]
                
                dic[h] = {"value" : self.value[i], "icon" : j, "color" : sym}
                h += 1
                
        return dic
    
    def shuffle(self):
        
        deck = fill_deck()
        
    
    



