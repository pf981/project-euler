import itertools
from functools import reduce
from operator import mul

from helpers import primes

RANGE_MAX = 11

def evenly_divisible(num):
    return all(num % x == 0 for x in range(1, RANGE_MAX))

def find_unsatisfied_divisors(num):
    return [x for x in range(1, RANGE_MAX) if num % x != 0]

def main():
    prime_factors = primes.prime_factors_range(RANGE_MAX)
    print(prime_factors)

    unique_factors = set(itertools.chain.from_iterable(prime_factors.values()))
    print(unique_factors)

    factors_counts = {}
    for factor in unique_factors:
        number_with_most_repeats_of_factor = max(prime_factors, key=lambda p: prime_factors[p].count(factor))
        factors_counts[factor] = prime_factors[number_with_most_repeats_of_factor].count(factor)

    print(factors_counts)



#    for vals in p.factors.values():
#    for vals in p.factors:
#        print(vals)
#
#    print(p.factors)
##    l = list(p.factors.values())
#
#    s = set(itertools.chain.from_iterable(l))
##    s = list(itertools.chain.from_iterable(l))
#    print(reduce(mul, s, 1)*2*2*3)
#    print(find_unsatisfied_divisors(reduce(mul, s, 1)))
##    next(x for x in range())
##    print(evenly_divisible(2520))
##    print(evenly_divisible(2521))

if __name__ == '__main__':
  main()
