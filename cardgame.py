from random import shuffle

class Card():
    suits = [ "spades" , "hearts" , "diamonds" , "clubs" ]
    values = [None,None,"2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" ,"10" , "Jack" , "Queen" , "King" , "Ace" ]
    """first two values are none to get the value and the index same"""
    def __init__(self,value,suit):
        """suit and value takes interger values so they can be used as index to access above list"""
        self.suit = suit
        self.value = value
    def __lt__(self,other):
        if self.value < other.value:
            return True
        elif self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        else:
            return False
        
    def __gt__(self,other):
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        else:
            return False
        
    def __repr__(self):
        return self.values[self.value] + ' of ' + self.suits[self.suit]


class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(0,4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def remove_first_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():
    def __init__(self,name):
        self.name = name
        self.card = None
        self.wins = 0
    

class Game():
    def __init__(self):
        self.deck = Deck()
        name1 = input("enter your name:")
        self.player1 = Player(name1)
        name2 = input("enter your name:")
        self.player2 = Player(name2)

    def playgame(self):
        print("war begins")
        responce = None
        
        while len(self.deck.cards) > 0:
            responce = input('q to quit and p to play:')
            if responce == 'q':
                break
            self.player1.card = self.deck.remove_first_card()
            self.player2.card = self.deck.remove_first_card()
            
            if self.player1.card > self.player2.card:
                self.player1.wins+=1
                print(f"{self.player1.name} won he pulled {self.player1.card} and {self.player2.name} pulled {self.player2.card}")
            else:
                self.player2.wins+=1
                print(f"{self.player2.name} won he pulled {self.player2.card} and {self.player1.name} pulled {self.player1.card}")
        print('The war is over. {} won and he had {} wins'.format(*self.winner()))

    def winner(self):
        if self.player1.wins > self.player2.wins:
            return self.player1.name,self.player1.wins
        else:
            return self.player2.name,self.player2.wins
        
game = Game()
game.playgame()

