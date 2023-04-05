import random
from cards import Card
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
class Deck():
    
    def __init__(self):
        
        self.all_cards= []
        
        for suit in suits:
            for rank in ranks:
                card_deck= Card(suit,rank)
                
                self.all_cards.append(card_deck)
    
    def shuffle(self):     
        random.shuffle(self.all_cards)
        
    def deal(self):
        delt_card = self.all_cards.pop(0)
        return delt_card