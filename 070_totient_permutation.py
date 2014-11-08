import math
import sympy

UPPER_BOUND = 10**7
# PRIMES = list(sympy.sieve.primerange(2, 1/2 * UPPER_BOUND))
PRIMES = list(sympy.sieve.primerange(2, 1.5 * math.sqrt(UPPER_BOUND)))
# PRIMES = list(sympy.sieve.primerange(2, math.sqrt(UPPER_BOUND)))

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

# Maybe keep a list of what is relatively prime to what

def main():
    answer = None
    best_ratio = None

    prime_pairs = ((p1, p2) for p1 in PRIMES for p2 in PRIMES)

    for p1, p2 in prime_pairs:
        # Construct n as the product of two primes
        n = p1 * p2

        if n > UPPER_BOUND:
            continue

        # As n is the product of two primes, the phi is simply (p1-1)(p2-1)
        totient = (p1 - 1) * (p2 - 1)

        if is_permutation(n, totient):
            print("@", n, totient)
            if not best_ratio or n / totient < best_ratio:
                answer = n
                best_ratio = n / totient

    print(answer)

if __name__ == '__main__':
    main()