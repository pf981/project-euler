import collections
import itertools
import sympy

def find_three_equally_spaced(prime_permuations):
#    distances = collections.defaultdict(int)
    distances = collections.defaultdict(list)
    #distances = {}

    # for i, prime1 in enumerate(prime_permuations):
    #     for prime2 in prime_permuations[i+1:]:
    #         distance = prime1 - prime2
    #         distances[distance].append((prime1, prime2))

    primes = sorted(prime_permuations)

    for i, prime1 in enumerate(primes):
        for prime2 in primes[i+1:]:
            distance = prime1 - prime2
            prime3 = prime2 + distance

            if prime3 in primes:
                return (prime1, prime2, prime3)

    return None
    # print(distances)
    # return [items for _, items in distances.items() if len(items) >= 2]

def main():
    primes = set(sympy.sieve.primerange(1000, 9999))

    # print(set(itertools.permutations("11")))
    # return
    #for i, prime in enumerate(primes):
    for prime in primes:
        prime_permuations = set(int(''.join(p))
                                for p in itertools.permutations(str(prime))
                                if int(''.join(p)) in primes)

        # print(prime, str(prime), prime_permuations)
        if len(prime_permuations) >= 3:
            # print(prime_permuations)
            # prime_permuations = sorted(list(prime_permuations))
            #if prime_permuations[1] - prime_permuations[0] == prime_permuations[2] - prime_permuations[1]:
            equally_spaced_primes = find_three_equally_spaced(list(prime_permuations))
            if equally_spaced_primes:
                print(equally_spaced_primes)
    answer = 0
    print(answer)


if __name__ == '__main__':
    main()
