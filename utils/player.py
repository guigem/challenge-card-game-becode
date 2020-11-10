from card import Card
import random


class Player:
    
    def __init__(self):
        
        obj = Card()
        self.cards = obj.fill_deck()
        self.turn_count = 0
        self.history = {}
        self.number_of_cards = len(self.history)

        
    def play(self):
        
        ran = random.randint(0, len(self.cards))
        self.history = {self.cards[ran]}
        print("{} {} played: {} {}".format(player_name, self.turn_count, dic[ran]["value"], dic[ran]["icon"]))
        #self.cards.pop(self.cards[ran])
        
        return self.cards[ran]
        
        


















obj = Card()
print(obj.icons)




value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
color = ["black", "red"]
icon = ["♥","♦","♣","♠"]

dic = {}
h = 0
for i in range(len(value)):
    for j in icon: 
        
        if j == "♥" or j == "♦":
            sym = color[1]
        else:
            sym = color[0]
        
        dic[h] = {"value" : value[i], "icon" : j, "color" : sym}
        h += 1
print(dic[2]["value"])

ty = []

for i in value:
    for j in icon:
        cd= i + j 
        ty.append(cd)

print(ty)
hands = [self.deck[i::n_players] for i in range(0, n_players)]
n_players = 6
tet = []
for i in range(n_players):
    inter = []
    for u in range(6):
        inter.append(ty[u])
    tet.append(inter)
    for o in inter:
        ty.remove(o)

    
print(tet)
    
print(len(dic))
ran = random.randint(0, len(dic))
print(ran)
import random

random.shuffle(dic)
print(dic)











