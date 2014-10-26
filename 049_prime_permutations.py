import collections
import itertools
import sympy

def find_three_equally_spaced(prime_permuations):
    """
    Returns a tuple of three equally spaced elements of prime_permutations in
    ascending order. None if no such tuple exists.
    """
    primes = sorted(prime_permuations)

    # For each distinct pair of elements
    for i, prime1 in enumerate(primes):
        for prime2 in primes[i+1:]:
            distance = prime2 - prime1
            prime3 = prime2 + distance

            # If there is an element that is the same distance away as the other two primes
            if prime3 in primes:
                # Then the three elements are the ones we are looking for
                return (prime1, prime2, prime3)
    # No three equally spaced
    return None

def main():
    # We are only interested in 4-digit primes
    primes = set(sympy.sieve.primerange(1000, 9999))

    # Triples is the set of three numbers satisfying the question. Note that
    # the example, (1487, 4817, 8147), will be in here too.
    triples = set()

    for prime in primes:
        # Find all the permutations
        prime_permuations = set(int(''.join(p))
                                for p in itertools.permutations(str(prime))
                                if int(''.join(p)) in primes)

        # If there were enough permutations to make a triple
        if len(prime_permuations) >= 3:
            # Try to find three equally spaced elements
            equally_spaced_primes = find_three_equally_spaced(list(prime_permuations))

            if equally_spaced_primes:
                triples.add(equally_spaced_primes)

    print(triples)

    # Exclude the example in the question (1487, 4817, 8147)
    correct_triple = next(triple for triple in triples if triple[0] != 1487)

    # Concatenate the triple into a 12-digit number
    answer = "".join(str(n) for n in correct_triple)

    print(answer)


if __name__ == '__main__':
    main()
