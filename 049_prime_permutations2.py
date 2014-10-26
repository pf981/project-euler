# This solution is much less efficient but slightly simpler
import collections
import itertools
import sympy

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


def find_prime_permutation_triple():
    # We are only interested in 4-digit primes
    primes = frozenset(sympy.sieve.primerange(1000, 9999))

    for prime1 in primes:
        # We are not interested in the example number in the question
        if prime1 == 1487:
            break

        # For every possible distance
        for distance in range(2, (9999 - prime1)//2, 2):
            prime2 = prime1 + distance
            prime3 = prime2 + distance

            # If all numbers are prime and permutations of each other
            if (prime2 in primes and prime3 in primes
              and is_permutation(prime1, prime2) and is_permutation(prime2, prime3)):
                return (prime1, prime2, prime3)

def main():
    answer = find_prime_permutation_triple()
    print(answer)


if __name__ == '__main__':
    main()
