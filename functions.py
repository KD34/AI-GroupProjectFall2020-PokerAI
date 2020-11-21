import random
from collections import defaultdict 
import sys

def calcFrequency(hand):
    freqDict = {}
    
    # Mark all array elements as not  visited
    visited = [False for i in range(len(hand))]
        
    #Traverse through array elements
    #and count frequencies

    for i in range(len(hand)):
        #Skip this element if already processed
        if visited[i] == True:
            continue
        
        #Count frequency
        count = 1
        for j in range (i + 1, len(hand), 1):
            if hand[i] == hand[j]:
                visited[j]  = True
                count += 1
        freqDict[hand[i]] = count
        
        print(hand[i], count)


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
    freqDict = {}
    freqDict = calcFrequency(hand)
    cardsWithPairs = []
    pairCount = 0
    pairPercentage = 0

    #Traverse through dictionary and check if there is a pair 
    for key in freqDict:
        if freqDict[key] == 2:
            print("This card has a pair of two")
            #add this card rank to an array
            cardsWithPairs.append(key)
    for card in range(len(cardsWithPairs)):
        if card in possibleCardsInDeck:
            pairCount = possibleCardsInDeck.count(card)
    
    pairPercentage = pairCount/len(possibleCardsInDeck)

    return pairPercentage

            


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


   





    







