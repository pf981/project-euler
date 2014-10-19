from math import factorial
from helpers import helpers

MAX_RANGE = 1000000

def is_curious(n):
    return n == sum(factorial(x) for x in helpers.int_to_digits(n))

def main():
    curious_nums = [n for n in range(3, MAX_RANGE) if is_curious(n)]

    print(curious_nums)
    print(sum(curious_nums))

if __name__ == '__main__':
    main()
