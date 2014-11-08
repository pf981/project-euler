# If we choose n such that n is the product of two primes (n = p*q), then we
# can calculate the totient as tot(n) = (p-1)(q-1).
#
# If we wish to minimise the ration of n to the totient, we have
#     n/tot(n) = p*q / ((p-1)(q-1))
# So we just have to find n=p*q that minimises p*q / ((p-1)(q-1))
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
    # Find p, q that minimises p*q / ((p-1)(q-1))
    best_pair = min(((p, q) for p in PRIMES for q in PRIMES),
                    key=lambda p,q: p*q/((p-1)*(q-1)))

    # n = p*q
    answer = best_pair[0] * best_pair[1]
    print(answer)

if __name__ == '__main__':
    main()