import enum
import re

# FIXME: Don't use globals
value_relation = {}
value_relation['T'] = 10
value_relation['J'] = 11
value_relation['Q'] = 12
value_relation['K'] = 13
value_relation['A'] = 14
for value in range(1, 10):
    value_relation[str(value)] = value
value_relation.update(dict(reversed(item) for item in value_relation.items()))


# The higher the number, the greater the value of the hand
# No need for royal flush as it is just a special case of a straight flush
BaseRanks = enum.Enum('BaseRanks', 'high_card one_pair two_pairs three_of_a_kind straight flush full_house four_of_a_kind straight_flush')


class Card:
    def __init__(self, card_string):
        # Convert the value to an integer
        self.value = value_relation[card_string[0]]

        # We can leave the suit as a char
        self.suit = card_string[1]

    def __repr__(self):
        return value_relation[self.value] + self.suit


def get_hand(hand_string):
    hand = [Card(card_string) for card_string in re.findall("\w\w", hand_string)]
    return sorted(hand, key=lambda card: card.value)


def rank_hand(hand):
    rank = [0]*10
    if all(card.suit == hand[0].suit for card in hand):
        rank[0] = BaseRanks.flush

    if all(card.value == hand[i-1].value + 1 for i, card in enumerate(hand[1:], start=1)):
        if rank[0] == BaseRanks.flush:
            rank[0] = BaseRanks.straight_flush
        else:
            rank[0] = BaseRanks.straight

        rank[1] = hand[-1]
        return rank

        # Royal flush
    return rank

def unit_tests():
    if rank_hand(get_hand("3C 5C 8C JC"))[0] == BaseRanks.flush:
        print("passed flush")
    else:
        print("FAILED FLUSH")

    if rank_hand(get_hand("8C 7D 9H TS"))[0] == BaseRanks.straight:
        print("passed straight")
    else:
        print("FAILED STRAIGHT")

    if rank_hand(get_hand("8D 7D 9D TD"))[0] == BaseRanks.straight_flush:
        print("passed straight flush")
    else:
        print("FAILED STRAIGHT FLUSH")

def main():
    # with open("p054_pokertest.txt") as in_file:
    #     text = in_file.read()

    # all_hands_string = re.findall("(.. .. .. .. ..) (.. .. .. .. ..)", text)
    # all_hands = [(get_hand(hand1), get_hand(hand2)) for hand1, hand2 in all_hands_string]

    unit_tests()
    # print(all_hands)


if __name__ == '__main__':
    main()