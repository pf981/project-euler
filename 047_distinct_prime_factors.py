import itertools
from helpers import helpers

NUM_CONSECUTIVE = 2

def main():
    for i in itertools.count(4):
        for num_consecutive in range(NUM_CONSECUTIVE):
            cur_factors = set(helpers.prime_factors(i + num_consecutive))

            # If there aren't the right number of factors
            if len(cur_factors) != NUM_CONSECUTIVE:
                break
        else:
            answer = i
            break


    print(answer)

if __name__ == '__main__':
    main()
