## trapoula kai na paiksoume mia apli

import random

cards = []  # empty list
figures = ["J", "Q", "K"]  # card figures
cardNo = [i for i in range(1, 11)] + figures  # cards
colors = ["Clubs", "Diamonds", "Spades", "Hearts"]

for i in cardNo:
    for j in colors:
        cards.append([i, j])

random.shuffle(cards)

player1 = []
player2 = []

player1.append(cards.pop())
player1.append(cards.pop())
player2.append(cards.pop())
player2.append(cards.pop())

print(player1)
print(player2)

p1score = 0
for card in player1:
    if card[0] in figures:
        p1score = p1score + 10
    else:
        p1score = p1score + card[0]

p2score = 0
for card in player2:
    if card[0] in figures:
        p2score = p2score + 10
    else:
        p2score = p2score + card[0]

print(p1score)
print(p2score)

if p1score > p2score:
    print("P1 wins")
elif p1score < p2score:
    print("P2 wins")
else:
    print("Draw...")
