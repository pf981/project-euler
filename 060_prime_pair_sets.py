import sympy
from sympy.ntheory.primetest import isprime

MAX_PRIMES = 10
TARGET_PAIRS = 4

def concat_ints(a, b):
    return int(str(a) + str(b))

def is_cat_pair(pair):
    return isprime(concat_ints(pair[0], pair[1])) and isprime(concat_ints(pair[0], pair[1]))

def main():
    primes = list(sympy.sieve.primerange(2, MAX_PRIMES))
    print(is_cat_pair((109, 673)))
    print(is_cat_pair((109, 674)))

    pairs = [(p1, p2)
             for i, p1 in enumerate(primes)
             for p2 in primes[i+1:]]

    print(primes)
    print(pairs)

    pass

if __name__ == '__main__':
    main()