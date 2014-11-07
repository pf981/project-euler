import collections
import sympy
from sympy.ntheory.primetest import isprime

MAX_PRIMES = 10
TARGET_PAIRS = 4

def concat_ints(a, b):
    return int(str(a) + str(b))

def is_cat_pair(pair):
    return isprime(concat_ints(pair[0], pair[1]))
    # return isprime(concat_ints(pair[0], pair[1])) and isprime(concat_ints(pair[0], pair[1]))

def main():
    primes = list(sympy.sieve.primerange(2, MAX_PRIMES))

    # all_pairs is a list of tuples of every combination of primes
    # FIXME: Maybe do all combinations, but only check the left concatenation
    all_pairs = [(p1, p2)
             for p1 in primes
             for p2 in primes]
    # all_pairs = [(p1, p2)
    #          for i, p1 in enumerate(primes)
    #          for p2 in primes[i+1:]]

    # special_pairs is a subset of all_pairs which only contains elements
    # whose pair can be concatenated to form a prime
    # paired_with = {p1: p2 for p1, p2 in all_pairs if is_cat_pair((p1, p2))}
    paired_with = collections.defaultdict(list)
    for p1, p2 in all_pairs:
        if is_cat_pair((p1, p2)):
            paired_with[p1].append(p2)

    print(paired_with)


    # special_pairs = [pair for pair in all_pairs if is_cat_pair(pair)]

    # for starter in primes:
    #     final_primes = [starter].extend(paired_with[starter])
    #     print(started, final_primes)


    # print(special_pairs)

    print(primes)
    # print(pairs)

    pass

if __name__ == '__main__':
    main()