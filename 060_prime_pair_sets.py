import collections
import copy
import sympy
from sympy.ntheory.primetest import isprime

MAX_PRIMES = 20
TARGET_PAIRS = 4

def concat_ints(a, b):
    return int(str(a) + str(b))

def is_cat_pair(pair):
    return isprime(concat_ints(pair[0], pair[1]))

def main():
    primes = list(sympy.sieve.primerange(2, MAX_PRIMES))

    all_pairs = [(p1, p2)
             for p1 in primes
             for p2 in primes]

    # paired_with maps a prime to a list of primes. This means that all the
    # elements in the value can be appended to the key to form a prime
    # paired_with[2] = [3, 11, 23] means that 23, 211 and 223 are all primes
    paired_with = collections.defaultdict(set)
    for p1, p2 in all_pairs:
        if is_cat_pair((p1, p2)):
            paired_with[p1].add(p2)
    # paired_with = collections.defaultdict(list)
    # for p1, p2 in all_pairs:
    #     if is_cat_pair((p1, p2)):
    #         paired_with[p1].append(p2)

    # print(paired_with)

    # Want:
    # 3  : 7 109 673
    # 7  : 3 109 673
    # 109: 3 7   673
    # 673: 3 7   109

    # THIS IS A TREE!!! - then maybe the pairs should be both concatenate so the tree is unidirectional
    #        3
    #   7   109    67

    for a in primes:
        final_primes = copy.copy(paired_with[a])
        for b in paired_with[a]:
            if b not in final_primes:
                continue
            final_primes &= paired_with[b]
        print(final_primes)


    # FIXME: Could trim the set by only considering primes who have 5 or more paired primes
    # for starter in primes:
    #     final_primes = copy.copy(paired_with[starter])
    #     for other in paired_with[starter]:
    #         if other not in final_primes:
    #             continue
    #         final_primes &= paired_with[other]
    #     print(final_primes)

        # final_primes = [starter] + paired_with[starter]
        # for other in final_primes:

        # print(starter, final_primes)

    print(primes)
    # print(pairs)

    pass

if __name__ == '__main__':
    main()