import collections
import itertools
import sys
from helpers import helpers

def is_pandigital(digits_string):
    #digits = list(helpers.int_to_digits(n))
    # print(len(set(digits)))
    # print("@@@")
    return len(digits_string) == len(set(digits_string))

# def is_pandigital(n):
#     digits = list(helpers.int_to_digits(n))
#     # print(len(set(digits)))
#     # print("@@@")
#     return len(digits) == len(set(digits))

def is_sub_string_divisible(digits_str):
    for i, prime in enumerate([2, 3, 5, 7, 11, 13 ,17], start=1):
        # If the substring doesn't satisfy the disivisibility criteria
        if int(digits_str[i:i+3]) % prime != 0:
            # print(digits_str[i:i+3], prime)
            return False
    return True


def main():
    # print(is_pandigital("12345"))
    # print(is_pandigital("123145"))
    print(is_sub_string_divisible("1406357289"))
    print(is_sub_string_divisible("1406357829"))
    # for s in itertools.permutations('1234567890'):
    #     print(s)
    return 0

if __name__ == '__main__':
    sys.exit(main())
