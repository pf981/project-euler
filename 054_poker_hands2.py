# This is a much more concise version based on KW.Diederich of the Project Euler forums
# https://projecteuler.net/thread=54;page=8

def rank(hand): # reduce the hand to some compact form that can be directly compared to another
    cards, colors = zip(*hand)
    cards = ['23456789TJQKA'.index(h) for h in cards]
    count, cards = zip(*sorted([(cards.count(h), h) for h in set(cards)], reverse=True))

    if len(cards) == 5:
        flush = (len(set(colors)) == 1)

        straight = (cards == tuple(cards[0]-i for i in range(5)))
        if cards == (12,3,2,1,0):
            straight = 1; cards = (3,)

        count = (((1,), (3,1,3)), ((3,1,2), (5,)))[straight][flush]

    return (count,cards)

def main():
    hands = (line.split() for line in open("p054_poker.txt"))
    player1, player2 = slice(0, 5), slice(5, 10)
    answer = sum(1 for hand in hands if rank(hand[player1]) > rank(hand[player2]))

    print(answer)

if __name__ == '__main__':
    main()