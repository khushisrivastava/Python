import random

suits=('Heart','Diamond','Spades','Clubes')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing=True


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+' of '+self.suit


class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        comp_deck=" "
        for card in self.deck:
            comp_deck+='\n'+Card.__str__()
            return 'The deck has:'+comp_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.ace=0

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]

        if card.rank=='Ace':
            self.ace+=1

    def adjust_for_ace(self):
        while self.value >21 and self.ace:
            self.value-=10
            self.ace-=1

class Chips:
    def __init__(self):
        self.total=100
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter your bet:"))
        except:
            print("Sorry! Please provide an integer.")
        else:
            if chips.bet>chips.total:
                print(f"Sorry, you do not have enough chips. You have {chips.total} chips.")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    #global playing
    while True:
        x=input('Hit or Stand? Enter h or s')

        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player Stands. Dealer's Turn")
            playing=False
        else:
            print("Could not undrestand.Enter h or s.")
            continue
        break

def show_some(player,dealer):
    print('DEALERS HAND:')
    print('One Card Hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print('DEALERS HAND:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)

def player_bust(player,dealer,chips):
    print('PLAYER BUST!!')
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print('PLAYER WINS!!')
    chips.win_bet()


def dealer_bust(player,dealer,chips):
    print('PLAYER WINS!! DEALER BUST!!')
    chips.win_bet()


def dealer_win(player,dealer,chips):
    print('PLAYER BUST!! DEALER WINS!!')
    chips.lose_bet()


def push(player,dealer):
    print('DEALER AND PLAYER TIE!! PUSH!')


while True:
    print("WELCOME TO BLACK JACK!!")
    deck=Deck()
    deck.shuffle()

    Player_hand=Hand()
    Player_hand.add_card(deck.deal())
    Player_hand.add_card(deck.deal())

    Dealer_hand=Hand()
    Dealer_hand.add_card(deck.deal())
    Dealer_hand.add_card(deck.deal())

    Player_chip=Chips()
    take_bet(Player_chip)

    show_some(Player_hand,Dealer_hand)

    while playing:
        hit_or_stand(deck,Player_hand)
        show_some(Player_hand,Dealer_hand)

        if Player_hand.value>21:
            show_all(Player_hand,Dealer_hand)
            player_bust(Player_hand,Dealer_hand,Player_chip)
            break
        elif Player_hand.value==21:
            show_all(Player_hand,Dealer_hand)
            player_wins(Player_hand,Dealer_hand,Player_chip)

    if Player_hand.value<21:
        while Dealer_hand.value<17:
            hit(deck,Dealer_hand)

        show_all(Player_hand,Dealer_hand)

        if Dealer_hand.value>21:
            dealer_bust(Player_hand,Dealer_hand,Player_chip)
        elif Dealer_hand.value>Player_hand.value:
            dealer_win(Player_hand,Dealer_hand,Player_chip)
        elif Dealer_hand.value<Player_hand.value:
            player_wins(Player_hand,Dealer_hand,Player_chip)
        else:
            push(Player_hand,Dealer_hand)

    print(f"Player chips are at {Player_chip.total}")

    new_game=input("would you like to play another hand? y/n")

    if new_game[0].lower=='y':
        playing=True
    else:
        print('Thank you for playing!')
        break
