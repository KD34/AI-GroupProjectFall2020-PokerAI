class CardSuit:

    suits = []

    def __init__(self):
        super().__init__()
        


    def addSuits(self):
        self.suits.append("Hearts")
        self.suits.append("Clubs")
        self.suits.append("Spades")
        self.suits.append("Diamonds")

    def getSuits(self):
        return self.suits
    
    