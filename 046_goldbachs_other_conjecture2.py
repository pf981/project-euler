import math
from helpers import helpers

MAX_RANGE = 10000

def is_square(num):
    root = math.sqrt(num)
    return root == int(root)

def get_smallest_not_satisfying_golbach():
    primes = []

    for candidate in range(3, MAX_RANGE, 2):
        # If it is a prime
        if helpers.is_prime(candidate):
            # Store it in the primes list
            primes.append(candidate)
        else:
            if not any(is_square((candidate - prime) / 2) for prime in primes):
                return candidate
            # for prime in primes:
            #     #if candidate == 5777:
            #     print(candidate, (candidate-prime)/2)
            #     # Check if it satisfies our criteria
            #     if not is_square((candidate - prime) / 2):
            #         return candidate


def main():
    # print(is_square(9))
    # print(is_square(10))
    answer = get_smallest_not_satisfying_golbach()
    print(answer)


if __name__ == '__main__':
    main()
