import math
import sympy

UPPER_BOUND = 10**7

# Initially, I tried only getting primes up to sqrt(UPPER_BOUND) but this was
# excluding many pairs whose product was still less than UPPER_BOUND. So I
# added 50% to the sqrt so we would encompass all prime pairs whose product
# was less than UPPER_BOUND
PRIMES = list(sympy.sieve.primerange(2, 1.5 * math.sqrt(UPPER_BOUND)))

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def main():
    answer = None
    best_ratio = None

    prime_pairs = ((p1, p2) for p1 in PRIMES for p2 in PRIMES)

    for p1, p2 in prime_pairs:
        # Construct n as the product of two primes
        n = p1 * p2

        if n > UPPER_BOUND:
            continue

        # As n is the product of two primes, phi is simply (p1-1)(p2-1)
        totient = (p1 - 1) * (p2 - 1)

        if is_permutation(n, totient):
            if not best_ratio or n / totient < best_ratio:
                answer = n
                best_ratio = n / totient

    print(answer)

if __name__ == '__main__':
    main()