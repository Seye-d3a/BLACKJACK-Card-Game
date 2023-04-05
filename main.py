import random
from cards import Card
from deck import Deck
from hand import Hand
from chips import Chips
from functions import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

game_on = True
while game_on:
    
    print("\nWelcome to Blackjack")
    
    #Create the deck and shuffle the cards
    game_deck = Deck()
    game_deck.shuffle()
    
    #Deal player's cards
    player_hand = Hand()
    player_hand.add_card(game_deck.deal())
    player_hand.add_card(game_deck.deal())
    
    #Deal Dealer's cards
    dealer_hand = Hand()
    dealer_hand.add_card(game_deck.deal()) 
    dealer_hand.add_card(game_deck.deal())
    
    #Set player's chips
    player_chips = Chips()
    
    playing = True
    while playing: #from our hit_stand function   
        #Take player's bet
        take_bet(player_chips)
    
        #Show cards but remember one of the dealer's cards stay hidden
        show_some(player_hand,dealer_hand)
        
        #ask player to hit or stand
        hit_stand(game_deck,player_hand)
        
        #show cards but one of the dealer's cards hidden
        show_some(player_hand,dealer_hand)
        
        #if player's hand exceeds 21
        if player_hand.value >21:
            player_bust(player_hand,dealer_hand,player_chips)
            break
        
        #If player doesn't bust, play dealer's hand till dealer_hand.value is 17
        if player_hand.value <=21:
            
            while dealer_hand.value <17:
                hit(game_deck,dealer_hand)
                
        #Show all cards
        show_all(player_hand,dealer_hand)
        
        #SCENARIOS FOR GAME TO END
        
        if dealer_hand.value >21:
            dealer_bust(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,player_chips)
        
        else:
            push(player_hand,dealer_hand)
            
        
        print(f"\n Player's chips total to: {player_chips.total}")
        
        if player_chips.total <= 0:
            print('\nTHE END')
            playing = False
            game_on = False
        
        else:
            continue

        #Ask to play again
        request = input("\nDo you want to play another hand? Enter y or n: ")
        
        if request[0].lower() == 'y':
            playing = True
            continue
        else:
            print('\nTHE END')
            playing = False
            game_on = False
