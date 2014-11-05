import enum
import re

value_relation = {}
value_relation['T'] = 10
value_relation['J'] = 11
value_relation['Q'] = 12
value_relation['K'] = 13
value_relation['A'] = 14
for value in range(1, 10):
    value_relation[str(value)] = value

class Card:
    def __init__(self, card_string):
        # Convert the value to an integer
        # if card_string[0] == 'T':
        #     self.value = 10
        # elif card_string[0] == 'J':
        #     self.value = 11
        # elif card_string[0] == 'Q':
        #     self.value = 12
        # elif card_string[0] == 'K':
        #     self.value = 13
        # elif card_string[0] == 'A':
        #     self.value = 14
        # else:
        #     self.value = int(card_string[0])
        self.value = value_relation[card_string[0]]

        # We can leave the suit as a char
        self.suit = card_string[1]

def get_hand(hand_string):
    print (re.findall("\w\w", hand_string))
    hand = [Card(card_string) for card_string in re.findall("\w\w", hand_string)]
    return hand

# The higher the number, the greater the value of the hand
BaseRanks = enum.Enum('BaseRanks', 'high_card one_pair two_pairs three_of_a_kind straight flush full_house four_of_a_kind straight_flush royal_flush')

def rank_hand(hand):
    rank = [0]*10
    # Royal flush
    pass


def main():
    with open("p054_poker.txt") as in_file:
        text = in_file.read()

    all_hands = re.findall("(.. .. .. .. ..) (.. .. .. .. ..)", text)
    for hand1, hand2 in all_hands:
#        print(hand1)
        print(get_hand(hand1))
    # print(all_hands)

if __name__ == '__main__':
    main()