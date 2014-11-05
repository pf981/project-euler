import enum
import re

# The higher the number, the greater the value of the hand
# No need for royal flush as it is just a special case of a straight flush
BaseRanks = enum.IntEnum('BaseRanks', 'high_card one_pair two_pairs three_of_a_kind straight flush full_house four_of_a_kind straight_flush')


def generate_value_relation():
    """
    This is a relation to convert character representations of card values to
    integer values and vice-versa. For example
        value_relation['K'] == 13
        value_relation[13] == 'K'
    """
    value_relation = {}

    # Picture cards
    value_relation['T'] = 10
    value_relation['J'] = 11
    value_relation['Q'] = 12
    value_relation['K'] = 13
    value_relation['A'] = 14

    # Number cards
    for value in range(1, 10):
        value_relation[str(value)] = value

    # Add the reverse relationship
    value_relation.update(dict(reversed(item) for item in value_relation.items()))

    return value_relation


class Card:
    value_relation = generate_value_relation()

    def __init__(self, card_string):
        # Convert the value to an integer
        self.value = Card.value_relation[card_string[0]]

        # We can leave the suit as a char
        self.suit = card_string[1]

    def __repr__(self):
        return Card.value_relation[self.value] + self.suit


def get_hand(hand_string):
    hand = [Card(card_string) for card_string in re.findall("\w\w", hand_string)]
    return sorted(hand, key=lambda card: card.value, reverse=True)


def rank_hand(hand):
    """
    Returns a tuple which represents the rank of the hand. Every hand's rank
    can be compared to every other hand's rank to determine the winner using
    the greater than operator.
    """
    base_rank = None
    secondary_rank = [card.value for card in hand]

    # Flush
    if all(card.suit == hand[0].suit for card in hand):
        base_rank = BaseRanks.flush

    # Straight
    if all(card.value == hand[i-1].value - 1 for i, card in enumerate(hand[1:], start=1)):
        if base_rank == BaseRanks.flush:
            base_rank = BaseRanks.straight_flush
        else:
            base_rank = BaseRanks.straight
        return tuple([int(base_rank)] + secondary_rank)

    # Four of a kind
    for i, card in enumerate(hand[3:], start=3):
        if card.value == hand[i-1].value == hand[i-2].value == hand[i-3].value:
            base_rank = BaseRanks.four_of_a_kind
            secondary_rank = [card.value] + [c.value for c in hand if c.value != card.value]
            return tuple([int(base_rank)] + secondary_rank)

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
        # If it's a member of an already discovered pair, ignore it
        if base_rank == BaseRanks.one_pair and card.value == secondary_rank[0]:
            continue

        # Bug if there's a 4 4 2 2 2
        if card.value == hand[i-1].value:
            if base_rank == BaseRanks.three_of_a_kind:
                base_rank = BaseRanks.full_house
                secondary_rank = [secondary_rank[0], card.value] + [c.value for c in hand if c.value != card.value and c.value != secondary_rank[0]]
                return tuple([int(base_rank)] + secondary_rank)
            elif base_rank == BaseRanks.one_pair:
                base_rank = BaseRanks.two_pairs
                secondary_rank = [secondary_rank[0], card.value] + [c.value for c in hand if c.value != card.value and c.value != secondary_rank[0]]
                return tuple([int(base_rank)] + secondary_rank)
            else:
                base_rank = BaseRanks.one_pair
                secondary_rank = [card.value] + [c.value for c in hand if c.value != card.value]

    if not base_rank:
        base_rank = BaseRanks.high_card

    return tuple([int(base_rank)] + secondary_rank)


def test_hand(hand_string, expected_rank):
    """
    This function is used in unit testing to check a hand against its expected
    rank string
    """
    rank = rank_hand(get_hand(hand_string))
    if rank == expected_rank:
        print("PASSED", hand_string, expected_rank)
    else:
        print("FAILED:")
        print("Hand:", hand_string)
        print("Expected:", expected_rank)
        print("Actual:", rank)
        print()


def unit_tests():
    test_hand("8D 7D 9C TD KH", [int(BaseRanks.high_card), 13, 10, 9, 8, 7])
    test_hand("8D 7D 8C TD KH", [int(BaseRanks.one_pair), 8, 13, 10, 7])
    test_hand("8D KD 8C TD KH", [int(BaseRanks.two_pairs), 13, 8, 10])
    test_hand("8D 7D 8C TD 8H", [int(BaseRanks.three_of_a_kind), 8, 10, 7])
    test_hand("8C 7D 9H TS 6H", [int(BaseRanks.straight), 10, 9, 8, 7, 6])
    test_hand("3C 5C 8C JC TC", [int(BaseRanks.flush), 11, 10, 8, 5, 3])
    test_hand("8D 7D 8C 7S 8H", [int(BaseRanks.full_house), 8, 7])
    test_hand("8D 7D 8C 8S 8H", [int(BaseRanks.four_of_a_kind), 8, 7])
    test_hand("8D 7D 9D TD JD", [int(BaseRanks.straight_flush), 11, 10, 9, 8, 7])

    # Ensure that it doesn't interpret a full house as two pair
    test_hand("4S 4H 4D 2S 2H", [int(BaseRanks.full_house), 4, 2])
    test_hand("4S 4H 2S 2H 2D", [int(BaseRanks.full_house), 4, 2])


def main():
    # unit_tests()

    with open("p054_poker.txt") as in_file:
        text = in_file.read()

    all_hands_string = re.findall("(.. .. .. .. ..) (.. .. .. .. ..)", text)
    all_hands = [(get_hand(hand1), get_hand(hand2)) for hand1, hand2 in all_hands_string]

    answer = sum(1 for hand1, hand2 in all_hands if rank_hand(hand1) > rank_hand(hand2))
    print(answer)

if __name__ == '__main__':
    main()