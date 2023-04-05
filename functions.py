
def take_bet(chips):
    while True:
        
        try:
            chips.bet = int(input("How much would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet>chips.total:
                print(f"Sorry you don't have enough chips! You have {chips.total}")
            else:
                break


def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.ace_adjust()

#Hit or Stand
def hit_stand(deck,hand):
    global playing
    
    while True:
        x = input("Hit or Stand? Enter h or s: ")
        
        if x[0].lower()== 'h':
            hit(deck,hand)
            
        elif x[0].lower()== 's':
            print("Player stands, Dealer's turn")
            playing = False
            
        else:
            print("Sorry, try again")
            continue
        break
    
def show_some(player,dealer):
    #Show only one of the dealer's cards
    print("\n Dealer's Hand: ")
    print("Unknown")
    print(dealer.cards[1])
    
    #Show all cards of the player
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    #Show dealers cards
    
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
   
    #calculate and display the value
    print(f"Value of Dealer's hand is {dealer.value}")
    
    #Show players cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
        
    #Calculate and display the value
    print(f"Value of Player's hand is {player.value}")


def player_bust(player,dealer,chips):
    print("\nPlayer BUST! Dealer Wins")
    chips.lose_bet()

def player_win(player,dealer,chips):
    print("\nPlayer Wins!")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("\nDealer BUST! Player Wins")
    chips.win_bet()

def dealer_win(player,dealer,chips):
    print("\nDealer Wins!")
    chips.lose_bet()

def push(player,dealer):
    print("\nGAME TIE")


