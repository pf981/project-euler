import collections
import itertools
import sympy

def find_three_equally_spaced(prime_permuations):
    primes = sorted(prime_permuations)

    for i, prime1 in enumerate(primes):
        for prime2 in primes[i+1:]:
            distance = prime2 - prime1
            prime3 = prime2 + distance

            if prime3 in primes:
                return (prime1, prime2, prime3)
    return None

def main():
    primes = set(sympy.sieve.primerange(1000, 9999))
    triples = set()

    for prime in primes:
        prime_permuations = set(int(''.join(p))
                                for p in itertools.permutations(str(prime))
                                if int(''.join(p)) in primes)

        if len(prime_permuations) >= 3:
            equally_spaced_primes = find_three_equally_spaced(list(prime_permuations))

            if equally_spaced_primes:
                triples.add(equally_spaced_primes)

    print(triples)
    correct_triple = next(triple for triple in triples if triple[0] != 1487)
    answer = "".join(str(n) for n in correct_triple)
    print(answer)


if __name__ == '__main__':
    main()
