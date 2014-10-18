from functools import reduce
from operator import mul

from helpers import primes

RANGE_MAX = 21


def main():
    # Find the prime factors of every number from 1 to 20
    prime_factors = primes.prime_factors_range(RANGE_MAX)

    answer_factors = []

    for key, value in prime_factors.items():
        answer_factors_copy = answer_factors[:]

        for factor in value:
            # If we don't already have this factor
            if not factor in answer_factors_copy:
                answer_factors.append(factor) # Store it
            else:
                # Remove the factor from the copy to ensure we keep repeat factors
                answer_factors_copy.remove(factor)

    # Multiply the factors together to get the answer
    answer = reduce(mul, answer_factors, 1)
    print(answer)


if __name__ == '__main__':
  main()
