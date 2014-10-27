import itertools
import sympy
#from sympy.ntheory.primetest import isprime
#from sympy.ntheory.primetest import primerange

PRIMES = set(sympy.primerange(1, 20000000))
MAX_PRIME = max(PRIMES)

def ratio_of_primes(nums):
    # return sum(1 for n in nums if isprime(n)) / len(nums)
    return sum(1 for n in nums if n in PRIMES) / len(nums)

def compute_min_length():
    diagonals = [1]
    cur_value = 1

    for spiral_radius in itertools.count(1):
        gap_between_diagonals = 2 * spiral_radius

        # For each corner
        for _ in range(4):
            cur_value += gap_between_diagonals
            diagonals.append(cur_value)

        #print(spiral_radius, diagonals)
        # print(spiral_radius*2 + 1, ratio_of_primes(diagonals))

        if cur_value > MAX_PRIME:
            return None

        print(ratio_of_primes(diagonals))
        if ratio_of_primes(diagonals) < 0.1:
            return spiral_radius * 2 + 1


def main():
    answer = compute_min_length()
    print(answer)


if __name__ == '__main__':
    main()
