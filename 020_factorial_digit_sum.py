import math
from helpers import helpers

def main():
    factorial = math.factorial(100)
    answer = sum(helpers.int_to_digits(factorial))
    print(answer)

if __name__ == '__main__':
  main()
