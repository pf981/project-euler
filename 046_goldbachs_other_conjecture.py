from helpers import helpers

MAX_RANGE = 10000
PRIMES = list(helpers.primes_to(MAX_RANGE))
SQUARES = list(helpers.squares_to(MAX_RANGE))
ODD_COMPOSITES = frozenset(2*n + 1 for n in range(1, MAX_RANGE // 2) if not 2*n + 1 in PRIMES)


def main():
    sums = frozenset(prime + 2*square for prime in PRIMES for square in SQUARES)
    answer = min(ODD_COMPOSITES - sums)
    print(answer)


if __name__ == '__main__':
    main()
