# Notes on optimisation: The algorithm I was using was good, but storing primes in a list
# had a MASSIVE performance hit compared to storing them as a frozenset. Simply switching to
# a set resulted in 940 times performance!!!
#
# And I believe I know why! This is because I frequently use (p in PRIMES) which is much faster
# on sets!
from helpers import helpers

# Timing using a frozenset
# real    0m1.186s
# user    0m1.041s
# sys     0m0.147s
PRIMES = frozenset(helpers.get_million_primes())

# Timing using a list
# real    18m35.668s
# user    18m29.080s
# sys     0m4.191s
# PRIMES = helpers.get_million_primes()

def is_double_truncated(prime):
    dividend = 10
    while dividend < prime:
        if prime % dividend not in PRIMES or prime // dividend not in PRIMES:
            return False
        dividend *= 10
    return True

def main():
    truncatable_primes = []

    # For each prime > 10
    for p in PRIMES:
        if is_double_truncated(p):
            truncatable_primes.append(p)
            print(p)
            if len(truncatable_primes) == 11 + 4: # +4 to not count 2,3,5&7
                break

    print(truncatable_primes)
    answer = sum(truncatable_primes)
    print(answer)

if __name__ == '__main__':
    main()
