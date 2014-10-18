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


# Note
# f([1, 2, 2, 3], [1, 2, 3]) -> True
# f([1, 2, 2, 3], [1, 1]) -> False
def contains_all_elements(original, elements):
    for element in elements:
        if not element in original:
            return False
        original.remove(element)
    return True

def main():
    # Find the prime factors of every number from 1 to 20
    prime_factors = primes.prime_factors_range(RANGE_MAX)

    answer_factors = []

    for key, value in prime_factors.items():
        answer_factors_copy = answer_factors[:]
        for factor in value:
#            print(answer_factors_copy)
#            print(factor)
            if not factor in answer_factors_copy:
                answer_factors.append(factor)
            else:
                answer_factors_copy.remove(factor)

#        if contains_all_elements(answer_factors, value):
#        print(key, value)

    print(answer_factors)

    answer = reduce(mul, answer_factors, 1)
    print(answer)


#    print(contains_all_elements([1, 2, 2, 3], [1, 2, 3]))
#    print(contains_all_elements([1, 2, 2, 3], [1, 1]))


if __name__ == '__main__':
  main()
