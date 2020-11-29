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
    card1  = hand.cards[0]
    card2 = hand.cards[1]
        

    deckRemainingSize = len(possibleCardsInDeck)

    #here is where you use if statements to check the probability of possible hands based on what's in the AI's hand



    
    winningChance = 0

    ##calculate the winning chance here


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
        cardDifference = 0

    return cardDifference



### here starts all of the hand probability calculations #####
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

    straightPct = 0
    deckRemainingSize = len(possibleCardsInDeck.cards)
    card1 = hand.cards[0]
    card2 = hand.cards[1]

    card1Rank = 0
    card2Rank = 0

    cardRankObj = CardRank()
    cardRankObj.addRanks()
    cardRanks = cardRankObj.getRanks()
    
    minCardValue = 0
    maxCardValue = 0
    straightPercentage = 0
    cardValue = 0


    fiveUpFromMinArr = [0] * 4
    fiveDownFromMaxArr = [0] * 4

 
    card1Rank = cardRanks[card1.rank]
    card2Rank = cardRanks[card2.rank]


    cardDifference = distanceBetweenCards(card1Rank, card2Rank)

    if cardDifference < 5 and cardDifference != 0:
        print("There is a possibility for a straight") 
        if card1Rank > card2Rank:
            maxCardValue = card1Rank
            minCardValue = card2Rank
        else:
            maxCardValue = card2Rank
            minCardValue = card1Rank

      

        #Five up from min card
        cardValue = minCardValue

        for x in range(4):
            if cardValue == 14:
                cardValue = 2
                fiveUpFromMinArr[x] = cardValue

            else:
                cardValue = cardValue + 1
                #print(cardValue)
                #put the card into the before array
                fiveUpFromMinArr[x] = cardValue

        #Five down from max card
        cardValue = maxCardValue   

        for x in range(4):
            if cardValue == 2:
                cardValue = 14
                fiveDownFromMaxArr[x] = cardValue


            else:
                cardValue = cardValue - 1
                #print(cardValue)
                #put the card into the before array
                fiveDownFromMaxArr[x] = cardValue

        upCount = 0
        downCount = 0  


        for rank in fiveDownFromMaxArr:
            if isRankInDeck(possibleCardsInDeck, rank):
                    downCount += 1
            
        for rank in fiveUpFromMinArr:
            if isRankInDeck(possibleCardsInDeck, rank):
                upCount =+1
        
        straightPct = max(upCount/deckRemainingSize, downCount/deckRemainingSize)

    return straightPct
        
        


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


    threeOfAKind = threeOfAKindProb(possibleCardsInDeck, hand)
    pairProb = pairProbability(possibleCardsInDeck, hand)
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
    

def straightFlushProb(possibleCardsInDeck, hand):
    flush = flushProb(possibleCardsInDeck, hand)
    straight = straightProb(possibleCardsInDeck, hand)
    straightFlush = flush * straight
    return straightFlush

def royalFlushProb(possibleCardsInDeck, hand):
    card1 = hand.cards[0]
    card2 = hand.cards[1]

    card1Rank = 0
    card2Rank = 0

    cardRankObj = CardRank()
    cardRankObj.addRanks()
    cardRanks = cardRankObj.getRanks()

    card1Rank = cardRanks[card1.rank]
    card2Rank = cardRanks[card2.rank]

    cardToCompare = None
    countSuits = 0


    part1Pct = 0
    part2Pct = 0

    ranksArr = [10, 11, 12, 13, 14]
    #Here I can remove the element that had the same rank as one of the AI's cards
    royalCards = []

    numOf10InDeck = numOfRankInDeck(possibleCardsInDeck, 10)
    numOfJInDeck = numOfRankInDeck(possibleCardsInDeck, 11)
    numOfQInDeck = numOfRankInDeck(possibleCardsInDeck, 12)
    numOfKInDeck = numOfRankInDeck(possibleCardsInDeck, 13)
    numOfAInDeck = numOfRankInDeck(possibleCardsInDeck, 14)
    deckRemainingSize = len(possibleCardsInDeck.cards)

    if card1Rank >= 10:
        cardToCompare = card1

    if card2Rank >= 10:
        cardToCompare = card2


    if card1Rank >= 10 or card2Rank >= 10:
        if isRankInDeck(possibleCardsInDeck, 10) and isRankInDeck(possibleCardsInDeck, 11) and isRankInDeck(possibleCardsInDeck, 12) and isRankInDeck(possibleCardsInDeck, 13) and isRankInDeck(possibleCardsInDeck, 14):
            part1Pct = (numOf10InDeck/deckRemainingSize) * (numOfJInDeck/(deckRemainingSize - 1)) * (numOfQInDeck/(deckRemainingSize - 2)) * (numOfKInDeck/(deckRemainingSize - 3)) * (numOfAInDeck/(deckRemainingSize - 4))
            
            #get all royal cards that are still in deck
            royalCards = getAllCardsOfCertainRanks(possibleCardsInDeck, ranksArr)

            countSuits = countCardsSameSuit(possibleCardsInDeck, cardToCompare, ranksArr)

            if countSuits == 4:
                part2Pct = (1/deckRemainingSize) * (1/deckRemainingSize - 1) * (1/deckRemainingSize - 2) * (1/deckRemainingSize - 3) * (1/deckRemainingSize - 4)
            
            else: 
                part2Pct = 0
        else:
            part1Pct = 0

        
    royalStraightFlushPct = part1Pct * part2Pct 

    return royalStraightFlushPct



### END PROBABOLITY CALCULATIONS HERE  ####
        


###Helper functions ####3

def numOfRankInDeck(deck, rank):
    cardRankObj = CardRank()
    cardRankObj.addRanks()
    cardRanks = cardRankObj.getRanks()

    count = 0

    for card in deck.cards:
        cardRank = cardRanks[card.rank]
        if cardRank == rank:
            count += 1

    return count

def isRankInDeck(deck, rank):
    cardRankObj = CardRank()
    cardRankObj.addRanks()
    cardRanks = cardRankObj.getRanks()


    for card in deck.cards:
        cardRank = cardRanks[card.rank]
        if rank == cardRank:
            return True
    return False


def getAllCardsOfCertainRanks(possibleCardsInDeck, ranks):
    cardsArr = []

    cardRankObj = CardRank()
    cardRankObj.addRanks()
    cardRanks = cardRankObj.getRanks()
    i = 0
    for card in deck.cards:
        cardRank = cardRanks[card.rank]
        for rank in ranks:
            if cardRank == rank:
                cardsArr.append(card)
                i += 1
    
    return cardsArr

def countCardsSameSuit (deck, cardToCompare, ranksArr):

    count = 0
    
    cardRankObj = CardRank()
    cardRankObj.addRanks()
    cardRanks = cardRankObj.getRanks()
    countOfSameSuitCards = 0

    #here is where we figure out what ranks are already in the player's hand
    #compare cardToCompare suit to the possible cards ranks in deck
    for card in deck.cards:
        cardRank = cardRanks[card.rank]
        if cardRank < 10:
            continue
        for rank in ranksArr:
            if cardRank == rank:
                if card.suit == cardToCompare.suit:
                    #print("Hey the " + str(card.toString()) + " has the same suit as " + str(cardToCompare.toString()))
                    count += 1
    
    return count
            



### These are some very bare bones functions that follow some of the steps in the model putside of the probability calculations  

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




##### "Main method" starts here #####

betLimit = 20

cards = []


deck = Deck(cards)


#Add all cards to the deck
deck.addAllCardsToDeck()
deck = shuffleDeck(deck)

AI = Player("AI")

#The dealHoleCards function is just the first round of the dealing cards - it explains in the model that 
# the dealer deals the flop, burn, turn, and river cards before round is completed - the deck and AI probability calculations
#will change based on the dealing of the rest of the
dealHoleCards(deck, AI)

#uncomment this to see what's in the AI's hand
#AI.toString()

#Call each probability function - i JUST call these functions at this point in order to see if everything is working
#where these functions are called will be changed when we write the round simulation code

pairProbability = pairProbability(deck, AI.hand)

twoPairsProbability = twoPairsProbability(deck, AI.hand)

threeOfAKindProb = threeOfAKindProb(deck, AI.hand)

flushProb = flushProb(deck, AI.hand)

fullHouseProb = threeOfAKindProb * pairProbability

fourOfAKindProb = fourOfAKindProb(deck, AI.hand)

straightProb = straightProb(deck, AI.hand)


straightFlushProb = straightProb * flushProb


royalStraightFlush = royalFlushProb(deck, AI.hand)





print("One Pair: " + str(pairProbability))
print("Two Pair: " + str(twoPairsProbability))
print("Three of a Kind: " + str(threeOfAKindProb))
print("Flush: " + str(flushProb))
print("Full House: " + str(fullHouseProb))
print("Four of a Kind: " + str(fourOfAKindProb))
print("Straight: " + str(straightProb))

#this is assuming that both cards are needed to be in the five card sequence
print("Straight flush: " + str(straightFlushProb))

print("Royal Straight Flush: " + str(royalStraightFlush))






   





    







