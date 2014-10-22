# The largest number that it could possibly be is x such that x + 2x = 987654321.
# This implies the largest pandigital is less than or equal to 329,218,107
import itertools
from helpers import helpers

PANDIGITAL_MULTIPLE_UPPER_BOUND = 329218107
#PERMUTATIONS = (helpers.list_to_int(x) for x in itertools.permutations(reversed(range(1, 10))))
PERMUTATIONS = (itertools.permutations(reversed(range(1, 10))))
# PERMUTATIONS = frozenset(itertools.permutations(reversed(range(1, 10))))

def get_largest_pandigital_multiple():
    # FIXME: This produces incorrect results as it incorrectly assumes n = 3
    for permutation in PERMUTATIONS:
        first = helpers.list_to_int(permutation[:3])
        second = helpers.list_to_int(permutation[3:6])
        third = helpers.list_to_int(permutation[6:])

        if first > second or second > third:
            continue

        if second % 2 == 0 and third % 3 == 0 and second // 2 == first and third // 3 == first:
            print(first, second, third)
            return first

# def get_largest_pandigital_multiple():
#     for num in reversed(range(1, PANDIGITAL_MULTIPLE_UPPER_BOUND + 1)):
#         digits = []
#         # print(num)
#         for multiplier in itertools.count(1):
#             digits.extend(list(helpers.int_to_digits(num * multiplier)))
#             # print(num, "*", multiplier, "=", num*multiplier)
#             # print(digits)

#             if len(digits) > 9:
#                 break
#             if len(digits) < 9 or multiplier == 1:
#                 continue
#             if tuple(digits) in PERMUTATIONS:
#                 return num

def main():
   answer = get_largest_pandigital_multiple()
   print(answer)

if __name__ == '__main__':
  main()
