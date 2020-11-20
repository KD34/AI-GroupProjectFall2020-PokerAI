import random
from collections import defaultdict 
import sys

def calcFrequency(arr):
    
    freq = [0] * len(arr)

    for x in arr:
        freq[x] = freq[x] + 1

    return freq
        



################ Dealer Functions ################
def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def dealHoleCards(deck, players):
    for x in range(2):
        for player in players:
            player.append(deck[x])

def dealFlopCards(deck):
    for x in range(3):
        flop[x] = deck[x]
    return flop

def dealBurnCard(deck):
    burnCard = deck.pop()
    return burnCard


def dealTurnCard(deck):
    turnCard = deck.pop()
    return turnCard


def dealRiverCard(deck):
    riverCard = deck.pop()
    return riverCard

    



################ AI Functions ################

def waitForNextRound():
    print("AI will wait for next round")

def leaveTable():
    print("AI left the table")
    sys.exit(0)

def bind():
    print("AI has entered the round")

def determineHandStrength(deck, possibleCardsInDeck, removedCardFromDeck, hand):
    hand.sort()

    winningChance = 0
    ######

    return winningChance



def twoCardsSameRank(possibleCardsInDeck, hand):

    freq = calcFrequency(hand)

def threeOfAKindProb(possibleCardsInDeck, hand):


def threeCardsSameRankProb(possibleCardsInDeck, hand):


def fiveCardsInSequenceProb(possibleCardsInDeck, hand):


def fiveCardsSameSuitProb(possibleCardsInDeck, hand):


def threeOfKindWithPairProb(possibleCardsInDeck, hand):

def fourOfAKindProb(possibleCardsInDeck, hand):

def fiveCardsSameSuitProb():
    straightFlush = fiveCardsSameSuitProb * fiveCardsInSequenceProb
    return straightFlush

def royalFlushProb():
    



def bet(winningChance):
    if winningChance >= 0.65:
        print("AI Will put more money in the pot")
    else:
        print("AI will not be this round")
}

     

def check(winningChance):
    if winningChance >= 0.40:
        print("AI can choose to check and bet zero")
    else:
        return






def revealHand(players):
    for player in players:
        for card in player.hand:
            print(card)


   





    







