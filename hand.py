
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
class Hand():
    
    def __init__(self):
        self.cards = [] #the player's hand
        self.value= 0 #the sum of the value of that hand
        self.aces=0 #Recall the ace rule of either 1 or 11
        
    def add_card(self,card):
        #card above is from the deal method in the deck class
        self.cards.append(card)
        self.value += values[card.rank]
    
        if card.rank == "Ace":
            self.aces +=1
        
    def ace_adjust(self):       
        while self.value >21 and self.aces>0:
            self.value -=10
            self.aces -=1
