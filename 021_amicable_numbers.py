import itertools
from helpers import helpers

MAX_RANGE = 10000

def d(n):
    return sum(helpers.factors(n)) - n

def main():
    answer = sum(n for n in range(2, MAX_RANGE) if d(d(n)) == n and d(n) != n)

    print(answer)

if __name__ == '__main__':
  main()
