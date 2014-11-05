# from sympy import sieve
import itertools
import re
import sympy

def any_length_combinations(l):
    combinations = []
    for i in range(len(l)):
        combinations += itertools.combinations(l, i+1)
    return combinations

def main():
    digits = 1
    # primes = list(sympy.sieve.primerange(10**(digits-1), 10**digits))

    # print(primes)
    # sieve.extend(10**digits)
    # print(sieve)
    # cur_prime = sympy.nextprime(2)

    while(True):
        primes = list(sympy.sieve.primerange(10**(digits-1), 10**digits))

        # combinations = itertools.combinations([0, 1, 2])
        # combinations = any_length_combinations([0,1,2])
        # print(combinations)
        combinations = any_length_combinations(range(digits))
        # print(combinations)

        for candidate in primes:
            for combination in combinations:
                matches = []
                for prime in primes:
                    regex = list(str(candidate))
                    for i in combination:
                        regex[i] = "."
                    regex = "".join(regex)

                    if re.match(regex, str(prime)):
                        matches.append(prime)
                print(candidate, matches)

        # Or just get all combinations of [0, 1, 2]. E.g. [0, 2] means you only keep the first and third digit
        # for prime in primes:
        #     max_mask = 0b111
        #     for mask in range(0b1, max_mask):
        #         print(bin(mask))

        digits += 1
        if digits == 3:
            break

if __name__ == '__main__':
    main()