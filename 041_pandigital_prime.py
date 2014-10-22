import itertools
from helpers import helpers

def find_biggest_pandigital_prime():
    # Starting from n = 10 digits, to n = 1 digit
    for max_range in reversed(range(1, 10)):
        # For each n-digit permutation
        for permutation in itertools.permutations(reversed(range(1, max_range))):
            num = helpers.list_to_int(permutation)
            if helpers.is_prime(num):
                return num

def main():
    answer = find_biggest_pandigital_prime()
    print(answer)

if __name__ == '__main__':
  main()
