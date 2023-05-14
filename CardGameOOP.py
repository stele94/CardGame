#### Card Game##########################################################
# - The game has 13 rounds:
#     - Each player plays 1 card.
#     - The player with highest card wins.
#     - Update the score for the winning hand.
#     - Print cards played in round and the winner (with winning card).
# - After the 13 rounds - print score for all players (P1, P2, P3, P4).
# - Print winner and score
########################################################################

import random


class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    ranks = ["2", "3", '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{Card.ranks[self.rank]} {Card.suits[self.suit]}"

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank


class Deck:
    def __init__(self):
        self.deck = []

        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))

        self.shuffle()

    def addCard(self, card):
        self.deck.append(card)

    def takeCard(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        deck = ""

        for card in self.deck:
            deck += "\n" + card.__str__()
        return "My deck: "+deck

    def __len__(self):
        return len(self.deck)


# Make Deck
deck = Deck()


class Player(Deck):
    def __init__(self, name):
        self.name = name.title()
        self.deck = []
        self.score = 0

    def __str__(self):
        return self.name + ': '+' '.join([str(card) for card in self.deck])

    def getName(self):
        return self.name

    def roundWinner(self):
        self.score += 1

    def winner(self):
        return self.score


players = [Player(f"P{i}") for i in range(1, 5)]

while len(deck) > 0:
    for player in players:
        player.addCard(deck.takeCard())


print(players[0])

# play 13 round the game
for i in range(1, 14):

    # Current cards on the board
    playedCards = []

    # User need to hit enter to play
    input("Press enter to play")

    for player in players:
        playedCards.append(player.takeCard())

    winnerCard = max(playedCards)
    winnerHand = players[playedCards.index(winnerCard)]
    winnerHand.roundWinner()

    print(f"Round:{i} "+" ".join(str(card) for card in playedCards) +
          f" Winner: {winnerHand.getName()} " + str(winnerCard))

for player in players:
    print(f"{player.getName()}: {player.winner()}")

# finding the highest score of players
playersScore = [player.winner() for player in players]
winnerCard = max(playersScore)


print(
    f"Winner is {players[playersScore.index(winnerCard)].getName()}:{winnerCard}")
