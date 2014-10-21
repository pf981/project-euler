import collections
import itertools
from helpers import helpers

def are_permutations(int_list):
    """
    Returns true if all the elements of int_list are permutations of each
    other. False otherwise.
    """
    for i, num in enumerate(int_list):
        digits = helpers.int_to_digits(num)

        if i == 0:
            first_counts = collections.Counter(digits)
            continue

        # Count each digit
        counts = collections.Counter(digits)

        # If an element of the list has a different digit count to the first,
        # it is not a permutation
        if counts != first_counts:
            return False
    return True

def main():
    for num in itertools.count(1):
        if are_permutations([num, 2*num, 3*num, 4*num, 5*num, 6*num]):
            answer = num
            break

    print(answer)

if __name__ == '__main__':
  main()
