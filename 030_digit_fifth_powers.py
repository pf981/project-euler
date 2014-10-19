from itertools import permutations
from helpers import helpers

POWER = 5

def main():
    correct_numbers = []
    for i in range(2, 1000000):
        if i == sum(x**POWER for x in helpers.int_to_digits(i)):
            correct_numbers.append(i)

    print(correct_numbers)

    answer = sum(correct_numbers)
    print(answer)


if __name__ == '__main__':
    main()
