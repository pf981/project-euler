import enum
import re
from helpers import helpers

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
BaseRanks = enum.IntEnum('BaseRanks', 'high_card one_pair two_pairs three_of_a_kind straight flush full_house four_of_a_kind straight_flush')


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
    return sorted(hand, key=lambda card: card.value, reverse=True)


def rank_hand(hand):
    base_rank = None
    secondary_rank = [card.value for card in hand]

    if all(card.suit == hand[0].suit for card in hand):
        base_rank = BaseRanks.flush

    if all(card.value == hand[i-1].value - 1 for i, card in enumerate(hand[1:], start=1)):
        if base_rank == BaseRanks.flush:
            base_rank = BaseRanks.straight_flush
        else:
            base_rank = BaseRanks.straight

    # Four of a kind
    for i, card in enumerate(hand[3:], start=3):
        if card.value == hand[i-1].value == hand[i-2].value == hand[i-3].value:
            base_rank = BaseRanks.four_of_a_kind
            secondary_rank = [card.value] + [c.value for c in hand if c.value != card.value]
            return [int(base_rank)] + secondary_rank

    # Three of a kind
    for i, card in enumerate(hand[2:], start=2):
        if card.value == hand[i-1].value == hand[i-2].value:
            base_rank = BaseRanks.three_of_a_kind
            secondary_rank = [card.value] + [c.value for c in hand if c.value != card.value]
            break

    # Pair
    for i, card in enumerate(hand[1:], start=1):
        # If the cards is a triple, ignore it
        if base_rank == BaseRanks.three_of_a_kind and card.value == secondary_rank[0]:
            continue
        if base_rank == BaseRanks.one_pair and card.value == secondary_rank[0]:
            continue

        if card.value == hand[i-1].value:
            if base_rank == BaseRanks.three_of_a_kind:
                base_rank = BaseRanks.full_house
                secondary_rank.append(card.value)
            elif base_rank == BaseRanks.one_pair:
                base_rank = BaseRanks.two_pairs
                secondary_rank = [secondary_rank[0], card.value] + [c.value for c in hand if c.value != card.value]
            else:
                base_rank = BaseRanks.one_pair
                secondary_rank = [card.value] + [c.value for c in hand if c.value != card.value]

    if not base_rank:
        base_rank = BaseRanks.high_card

    return [int(base_rank)] + secondary_rank # and others

def rank_hand_int(hand):
     rank = rank_hand(hand)
 #    print(repr(rank[0]))
     return sum((value*(10**(10-i)) for i, value in enumerate(rank)))

def unit_tests():
     if rank_hand(get_hand("8D 7D 9C TD KH"))[0] == BaseRanks.high_card:
         print("passed high card")
     else:
         print("FAILED HIGH CARD")

     if rank_hand(get_hand("8D 7D 8C TD KH"))[0] == BaseRanks.one_pair:
         print("passed one pair")
     else:
         print("FAILED ONE PAIR")

     if rank_hand(get_hand("8D KD 8C TD KH"))[0] == BaseRanks.two_pairs:
         print("passed two pair")
     else:
         print("FAILED TWO PAIR")

     if rank_hand(get_hand("8D 7D 8C TD 8H"))[0] == BaseRanks.three_of_a_kind:
         print("passed three of a kind")
     else:
         print("FAILED THREE OF A KIND")

     if rank_hand(get_hand("8C 7D 9H TS 6H"))[0] == BaseRanks.straight:
         print("passed straight")
     else:
         print("FAILED STRAIGHT")

     if rank_hand(get_hand("3C 5C 8C JC"))[0] == BaseRanks.flush:
         print("passed flush")
     else:
         print("FAILED FLUSH")

     if rank_hand(get_hand("8D 7D 8C 7S 8H"))[0] == BaseRanks.full_house:
         print("passed full house")
     else:
         print("FAILED FULL HOUSE")
         print(rank_hand(get_hand("8D 7D 8C 7S 8H")))

     if rank_hand(get_hand("8D 7D 8C 8S 8H"))[0] == BaseRanks.four_of_a_kind:
         print("passed four of a kind")
     else:
         print("FAILED four of a kind")

     if rank_hand(get_hand("8D 7D 9D TD JD"))[0] == BaseRanks.straight_flush:
         print("passed straight flush")
     else:
         print("FAILED STRAIGHT FLUSH")


def main():
     with open("p054_poker.txt") as in_file:
         text = in_file.read()

     all_hands_string = re.findall("(.. .. .. .. ..) (.. .. .. .. ..)", text)
     all_hands = [(get_hand(hand1), get_hand(hand2)) for hand1, hand2 in all_hands_string]

     # for hand1, hand2 in all_hands:
     #    if rank_hand_int(hand1) > rank_hand_int(hand2):
     #        print(hand1, " > ", hand2)
     #    else:
     #        print(hand1, " < ", hand2)
     # unit_tests()
     # print(all_hands)
     # print(all_hands)
     answer = sum(1 for hand1, hand2 in all_hands if rank_hand_int(hand1) > rank_hand_int(hand2))
     print(answer)


if __name__ == '__main__':
     main()