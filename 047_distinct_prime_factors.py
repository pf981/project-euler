import itertools
from helpers import helpers

NUM_CONSECUTIVE = 4

def satisfies_criteria(candidate):
    for num_consecutive in range(NUM_CONSECUTIVE):
        cur_factors = set(helpers.prime_factors(candidate + num_consecutive))

        # If there aren't the right number of factors
        if len(cur_factors) != NUM_CONSECUTIVE:
            return False
    return True


def main():
    for candidate in itertools.count(4):
        if satisfies_criteria(candidate):
            answer = candidate
            break

    print(answer)

if __name__ == '__main__':
    main()
