from Deck import Deck 

class Player:

   
   
    hand = Deck(cards = [])

    def __init__(self, name):
        super().__init__()
        self.name = name
        


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def getHand(self):
        return self.hand
    
    def setHand(self, hand):
        self.hand = hand

    def toString(self):
        return str(self.name) + str(self.hand.toString())
    


