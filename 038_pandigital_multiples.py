# This solution assumes n=2. If this solution failed, I would rewrite it with
# n=3 and n=4, but this solution is sufficient.
import itertools
from helpers import helpers

PERMUTATIONS = (itertools.permutations(reversed(range(1, 10))))

def get_largest_pandigital_multiple():
    # For each permutation
    for permutation in PERMUTATIONS:
        # Split the permutation in two. Note that the only split that makes
        # sense is the the first being 4 digits and the second being 5
        # digits. This is because second = 2*first.
        first = helpers.list_to_int(permutation[:4])
        second = helpers.list_to_int(permutation[4:])

        if second == 2 * first:
            return int(str(first) + str(second))

def main():
   answer = get_largest_pandigital_multiple()
   print(answer)

if __name__ == '__main__':
  main()
