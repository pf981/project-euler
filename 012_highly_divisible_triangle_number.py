import itertools
from helpers import helpers

MIN_DIVISORS = 500

def triangle_numbers():
    """Generates the first million triangle numbers"""
    triangle_num = 0
    for i in range(1, 1000000):
        triangle_num += i
        yield triangle_num

def main():
    for triangle_num in triangle_numbers():
        # If it has enough divisors to be the solution
        if len(helpers.factors(triangle_num)) > MIN_DIVISORS:
            answer = triangle_num
            break

    print(answer)


if __name__ == '__main__':
  main()
