from helpers import helpers

MAX_RANGE = 10000
PRIMES = list(helpers.primes_to(MAX_RANGE))
SQUARES = list(helpers.squares_to(MAX_RANGE))
ODD_COMPOSITES = frozenset(2*n + 1 for n in range(1, MAX_RANGE // 2) if not 2*n + 1 in PRIMES)


def main():
    # print(ODD_COMPOSITES)
    # print(PRIMES)
    # for prime in PRIMES:
    #     # print(prime)
    #     for square in SQUARES:
    #         # print(prime, square, prime + 2*square)
    #         print(prime)
    #     print()

    sums = frozenset(prime + 2*square for prime in PRIMES for square in SQUARES)
    # sums = sorted(list(prime + 2*square for prime in PRIMES for square in SQUARES))
    # print(sums)

    answer = min(ODD_COMPOSITES - sums)
    print(answer)


if __name__ == '__main__':
    main()
