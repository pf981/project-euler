import itertools
from functools import reduce
from operator import mul

from helpers import primes

RANGE_MAX = 21


# This function is unused
def evenly_divisible(num):
    return all(num % x == 0 for x in range(1, RANGE_MAX))


# This function is unused
def find_unsatisfied_divisors(num):
    return [x for x in range(1, RANGE_MAX) if num % x != 0]


def main():
    # Find the prime factors of every number from 1 to 20
    prime_factors = primes.prime_factors_range(RANGE_MAX)

    # Find the unique list of prime factors
    unique_factors = set(itertools.chain.from_iterable(prime_factors.values()))

    # Count how many times each prime occurs in each number
    factors_counts = {}
    for factor in unique_factors:
        number_with_most_repeats_of_factor = max(prime_factors, key=lambda p: prime_factors[p].count(factor))
        factors_counts[factor] = prime_factors[number_with_most_repeats_of_factor].count(factor)

    # Determine the number with the most occurances of each prime
    # Calculate factor^count_of_that_factor
    all_factors_of_answer = [pow(factor, factors_counts[factor]) for factor in factors_counts]

    # Multiply all these factors together to get the answer
    answer = reduce(mul, all_factors_of_answer, 1)

    print(answer)


if __name__ == '__main__':
  main()
