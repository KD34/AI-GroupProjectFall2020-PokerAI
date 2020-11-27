from Card import Card
from CardRank import CardRank
from CardSuit import CardSuit


class Deck:
    def __init__(self, cards):
        super().__init__()
        self.cards = cards

    def addCardToDeck(self, card):
        self.cards.append(card)

    def removeCardFromDeck(self, card):
        self.cards.remove(card)


    def addAllCardsToDeck(self):
        suits = []
        ranks = []   

        cardRanks = CardRank()
        cardSuits = CardSuit()

        cardRanks.addRanks()
        cardSuits.addSuits()

        for i in range(len(cardSuits.suits)):
            for rank in cardRanks.ranks.keys():
                self.addCardToDeck(Card(rank, cardSuits.suits[i]))

    def toString(self):
        for card in self.cards:
             print(card.toString())

    
    def dealCard(self):
        removeCardFromDeck(self.cards[0])

       

    def isEmpty(self):
        if not self.cards:
            return True
        else:
            return False
    
    def getDeckOfCards(self):
        return self.cards

    def setDeckOfCards(self, cards):
        self.cards = cards

    
    

    