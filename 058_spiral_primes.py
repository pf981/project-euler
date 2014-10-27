import itertools
from sympy.ntheory.primetest import isprime

def compute_min_length():
    cur_value = 1
    num_primes = 0

    for spiral_radius in itertools.count(1):
        gap_between_diagonals = 2 * spiral_radius

        # For each of the first three corners
        for _ in range(3):
            cur_value += gap_between_diagonals
            if isprime(cur_value):
                num_primes += 1

        # Ignore the bottom right corner
        cur_value += gap_between_diagonals

        # There are 4 corners in each spiral, and one center number
        prime_ratio_of_diagonal = num_primes / (4 * spiral_radius + 1)
        if prime_ratio_of_diagonal < 0.1:
            return spiral_radius * 2 + 1


def main():
    answer = compute_min_length()
    print(answer)


if __name__ == '__main__':
    main()
