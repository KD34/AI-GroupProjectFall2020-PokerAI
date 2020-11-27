import random
from collections import defaultdict 
import sys

from Deck import Deck
from Card import Card
from CardRank import CardRank
from CardSuit import CardSuit
from Player import Player




def calcFrequencyOfRanks(deck, card):
    freqDict = {}
    count = 0
    
    #calculate the frequency of the rank of the given card within the deck

    for x in deck.cards:
        if x.rank == card.rank:
            freqDict[card] = count + 1
            count = count + 1

    return freqDict

def calcFrequencyOfSuits(deck, card):
    freqDict = {}
    count = 0
    
    #calculate the frequency of the rank of the given card within the deck

    for x in deck.cards:
        if x.suit == card.suit:
            freqDict[card] = count + 1
            count = count + 1

    return freqDict


################ Dealer Functions ################
def shuffleDeck(deck):
    random.shuffle(deck.cards)
    return deck

def dealHoleCards(deck, AI):
    for x in range(2):
        AI.hand.addCardToDeck(deck.cards[0])
        deck.removeCardFromDeck(deck.cards[0])
        deck = shuffleDeck(deck)
    return deck

       
def dealFlopCards(deck, AI):
    flopCards = []
    for x in range(3):
        AI.hand.addCardToDeck(deck.cards[0])
        flopCards[x] = deck.cards[0]
        deck.removeCardFromDeck(deck.cards[0])
        deck = shuffleDeck(deck)
    return deck, flopCards

def dealBurnCard(deck):
    burnCard = deck.pop()
    AI.hand.addCardToDeck(deck.cards[0])
    deck.removeCardFromDeck(deck.cards[0])
    deck = shuffleDeck(deck)
    return deck, burnCard


def dealTurnCard(deck):
    turnCard = deck.pop()
    AI.hand.addCardToDeck(deck.cards[0])
    deck.removeCardFromDeck(deck.cards[0])
    deck = shuffleDeck(deck)
    return deck, turnCard


def dealRiverCard(deck):
    riverCard = deck.pop()
    AI.hand.addCardToDeck(deck.cards[0])
    deck.removeCardFromDeck(deck.cards[0])
    deck = shuffleDeck(deck)
    return deck, riverCard

    



################ AI Functions ################

def waitForNextRound():
    print("AI will wait for next round")
    #Call AIStartPhase

def leaveTable():
    print("AI left the table")
    sys.exit(0)

def bind():
    print("AI has entered the round and placed a bet")

def determineHandStrength(deck, possibleCardsInDeck, removedCardFromDeck, hand):
    hand.sort()
    card1  = hand[0]
    card2 = hand[1]
        

    deckRemainingSize = len(possibleCardsInDeck)

    #if card1 in deck or card2 in deck:
        #call twoCardsSameRank function
    
    #two different pairs if statement

    #elif card1 in deck and card2 in deck:
        #call threeCardsSameRank function

    #figure out how to call flush function



    winningChance = 0
    ######

    return winningChance


#def AIStartPhase():

    #choiceArr = ["bind", "no bind", "leave"]

    #pick random element from choice arr
        #decsion = elemetFromChoiceArray
    #if AI chooses bind:
        #call function that runs option for bind
    #if AI chooses no bind
        #call function that runs option for bind
    #if AU chooses leave:
        #call function that runs option for leave


#def AIActingPhase():
    #call check strengthOfHand function

    #if AI has a pair in hand
        #call check function
        #increment numberOfChecks

    #if AI has a pair in hand AND other players Raise OR Bet
        #call AI match function
        #subtract current money that AI has

    #if AI had no pair in hand
        #if players Bet or Raise AND AI has >= 30% og getting one of the desired hands
            #AI matched bets "Call"
        #if players Bet or RAISE AND AI had < 20% chance of getting one of the desired hands
            #call AI fold function
            #AI Losses "money"
        #    
        
         



def distanceBetweenCards(card1Rank, card2Rank):
    cardDifference = 0

    if card1Rank > card2Rank:
        cardDifference = card1Rank - card2Rank
    elif card2Rank > card1Rank:
        cardDifference = card2Rank - card1Rank
    else:
        print("cards have the same rank")



def pairProbability(possibleCardsInDeck, hand):

    card1 = hand.cards[0]
    card2 = hand.cards[1]

    #possibleCardsInDeck.removeCardFromDeck(card1)
    #possibleCardsInDeck.removeCardFromDeck(card2)

    freqCard1 = {}
    freqCard2 = {}

    card1Count = 0
    card2Count = 0

    #calculate frequency of card1
    freqCard1 = calcFrequencyOfRanks(possibleCardsInDeck, card1)
    #calculate the frequency of card2
    freqCard2 = calcFrequencyOfRanks(possibleCardsInDeck, card2)
    
    pairCount = 0
    pairPercentage = 0


     
    card1Count = freqCard1[card1]
    card2Count = freqCard2[card2]

    pairCount = card1Count + card2Count
    
    pairPercentage = pairCount/len(possibleCardsInDeck.cards)

    return pairPercentage


def twoPairsProbability(possibleCardsInDeck, hand):
    card1 = hand.cards[0]   
    card2 = hand.cards[1]

    #possibleCardsInDeck.removeCardFromDeck(card1)
    #possibleCardsInDeck.removeCardFromDeck(card2)

    freqCard1 = {}
    freqCard2 = {}

    card1Count = 0
    card2Count = 0

    pairCount = 0
    pairPercentage = 0

    #calculate frequency of card1
    freqCard1 = calcFrequencyOfRanks(possibleCardsInDeck, card1)
    #calculate the frequency of card2
    freqCard2 = calcFrequencyOfRanks(possibleCardsInDeck, card2)
    
    pairCount = 0
    pairPercentage = 0

     
    card1Count = freqCard1[card1]
    card2Count = freqCard2[card2]

    pairCount = card1Count + card2Count
    
    pairPercentage = (card1Count/len(possibleCardsInDeck.cards)) * (card2Count/len(possibleCardsInDeck.cards))

    return pairPercentage



def threeOfAKindProb(possibleCardsInDeck, hand):
    card1 = hand.cards[0]   
    card2 = hand.cards[1]

    #possibleCardsInDeck.removeCardFromDeck(card1)
    #possibleCardsInDeck.removeCardFromDeck(card2)

    freqCard1 = {}
    freqCard2 = {}

    card1Count = 0
    card2Count = 0

    threeOfAKindCount = 0
    threeOfAKindPct = 0

    #calculate frequency of card1
    freqCard1 = calcFrequencyOfRanks(possibleCardsInDeck, card1)
    #calculate the frequency of card2
    freqCard2 = calcFrequencyOfRanks(possibleCardsInDeck, card2)
    
     
    card1Count = freqCard1[card1]
    card2Count = freqCard2[card2]

    threeOfAKindCount = card1Count + card2Count
    
    threeOfAKindPct = (threeOfAKindCount/ len(possibleCardsInDeck.cards))

    return threeOfAKindPct
    


def straightProb(possibleCardsInDeck, hand):
    card1 = hand.cards[0]
    card2 = hand.cards[1]
    straightPercentage = 0

    cardDifference = distanceBetweenCards(card1.rank, card2.rank)

    if cardDifference <= 5:
        ("There is a possibility for a straight")    

    #straightPercentage = (number possibleValues left in deck by array/deckRemaingSize)

def flushProb(possibleCardsInDeck, hand):
    card1 = hand.cards[0]
    card2 = hand.cards[1]

    card1Count = 0
    card2Count = 0

    freqCard1 = {}
    freqCard2 = {}

    flushPct = 0


    freqCard1 = calcFrequencyOfSuits(possibleCardsInDeck, card1)
    freqCard2 = calcFrequencyOfSuits(possibleCardsInDeck, card2)

    card1Count = freqCard1[card1]
    card2Count = freqCard2[card2]
  

    flushPct = max((card1Count/len(possibleCardsInDeck.cards)), (card2Count/len(possibleCardsInDeck.cards)))

    return flushPct
    
    

def fullHouseProb(possibleCardsInDeck, hand):
    threeOfAKind = 0.0
    pairProb = 0.0


    threeOfAKind = float(threeOfAKindProb(possibleCardsInDeck, hand))
    pairProb = float(pairProbability(possibleCardsInDeck, hand))
    fullHouseProb = threeOfAKind * pairProb

    return fullHouseProb

def fourOfAKindProb(possibleCardsInDeck, hand):

    fourOfAKindProb = 0
    fourOfAKindProbCard1 = 0
    fourOfAKindProbCard2 = 0

    card1 = hand.cards[0]
    card2 = hand.cards[1]

    card1Count = 0
    card2Count = 0

    freqCard1 = {}
    freqCard2 = {}


    freqCard1 = calcFrequencyOfRanks(possibleCardsInDeck, card1)
    freqCard2 = calcFrequencyOfRanks(possibleCardsInDeck, card2)

    card1Count = freqCard1[card1]
    card2Count = freqCard2[card2]

    deckRemainingSize = len(possibleCardsInDeck.cards)

    if card1.rank != card2.rank:
        if card1Count >= 3:
            fourOfAKindProbCard1 = (card1Count/deckRemainingSize) * (card1Count - 1/ deckRemainingSize - 1 ) * (card1Count -2 / deckRemainingSize - 2) 
        if card2Count>= 3:
            fourOfAKindProbCard2 = (card2Count/deckRemainingSize) * (card2Count - 1/ deckRemainingSize - 1 ) * (card2Count -2 / deckRemainingSize - 2)

        fourOfAKindProb = fourOfAKindProbCard1 + fourOfAKindProbCard2     

    elif card1.rank == card2.rank:
        fourOfAKindProb = (card1Count/deckRemainingSize) * (card1Count - 1/ deckRemainingSize - 1 )


    return fourOfAKindProb
    

def straightFlushProb():
    straightFlush = fiveCardsSameSuitProb * fiveCardsInSequenceProb
    return straightFlush

def royalFlushProb(possibleCardsInDeck, hand):
    card1 = hand[0]
    card2 = hand[1]

    part1Pct = 0
    part2Pct = 0

    numOf10InDeck = numOfRankInDeck(possibleCardsInDeck, 10)
    numOfJInDeck = numOfRankInDeck(possibleCardsInDeck, 11)
    numOfQInDeck = numOfRankInDeck(possibleCardsInDeck, 12)
    numOfKInDeck = numOfRankInDeck(possibleCardsInDeck, 13)
    numOfAInDeck = numOfRankInDeck(possibleCardsInDeck, 14)
    deckRemainingSize = len(possibleCardsInDeck)



    #if card1.rank >= 10 or card2.rank >= 10:
        #if isRankInDeck(possibleCardsInDeck, 10) and isRankInDeck(possibleCardsInDeck, 11) and isRankInDeck(possibleCardsInDeck, 12) and isRankInDeck(possibleCardsInDeck, 13) and isRankInDeck(possibleCardsInDeck, 14):
            #part1Pct = (numOf10InDeck/deckRemainingSize * (numOfJInDeck/deckRemainingSize-1) * (numOfQInDeck/deckRemainingSize-2) * (numOfKInDeck/deckRemainingSize -3) * (numOfAInDeck/deckRemainingSize - 4)
        
        #else:
            #part1Pct = 0


        #if isAllCardsSameSuit(possibleCardsInDeck, card10, cardJ, cardQ, cardK, cardA):
            #part2Pct = (1/deckRemainingSize) * (1/deckRemainingSize - 1) * (1/deckRemainingSize - 2) * (1/deckRemainingSize - 3) * (1/deckRemainingSize - 4)

        #else:
            #part2Pct = 0

        
        #royalSraightFlushPct = part1Pct * part2Pct 

        #return royalSraightFlushPct
        


def numOfRankInDeck(deck, rank):
    count = 0

    for card in deck:
        if card.rank == rank:
            count += 1

    return count

def isRankInDeck(deck, rank):

    for card in deck:
        if rank in deck:
            return True
    return False

def isAllCardsSameSuit (deck, card1, card2, card3, card4, card5):
    allCardsInDeck = False

    if isRankInDeck(deck, card1.rank) and isRankInDeck(deck, card2.rank) and isRankInDeck(deck, card3.rank) and isRankInDeck(deck, card4.rank) and isRankInDeck(deck, card5.rank):

        if card1.suit == card2.suit and card2.suit == card3.suit and card3.suit == card4.suit and card4.suit == card5.suit:
            return True

        else:
            return False



def bet(winningChance):
    if winningChance >= 0.65:
        print("AI Will put more money in the pot")
    else:
        print("AI will not be this round")


     

def check(winningChance):
    if winningChance >= 0.40:
        print("AI can choose to check and bet zero")
    else:
        return



def revealHand(players):
    for player in players:
        for card in player.hand:
            print(card)


#def firstRound():

#def secondRound():

#def thirdRound():





betLimit = 20

cards = []


deck = Deck(cards)

#player1 = Player("Sue")
#player2 = Player("Our AI")

#players = [player1, player2]


deck.addAllCardsToDeck()
deck = shuffleDeck(deck)

AI = Player("AI")


dealHoleCards(deck, AI)

AI.toString()

#Call each probability function
pairProbability = pairProbability(deck, AI.hand)

twoPairsProbability = twoPairsProbability(deck, AI.hand)

threeOfAKindProb = threeOfAKindProb(deck, AI.hand)

flushProb = flushProb(deck, AI.hand)

# fix full house float error
fullHouseProb = threeOfAKindProb * pairProbability

fourOfAKindProb = fourOfAKindProb(deck, AI.hand)





print("One Pair: " + str(pairProbability))
print("Two Pair: " + str(twoPairsProbability))
print("Three of a Kind: " + str(threeOfAKindProb))
print("Flush: " + str(flushProb))
print("Full House: " + str(fullHouseProb))
print("Four of a Kind: " + str(fourOfAKindProb))
#deck.toString()






   





    







