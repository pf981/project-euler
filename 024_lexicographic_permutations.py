from itertools import permutations
from helpers import helpers

DIGITS = "0123456789"
ELEMENT_TO_GET = 1000000

def main():
    answer = helpers.get_nth_element_of_generator(permutations(DIGITS), ELEMENT_TO_GET - 1)
    answer = "".join(answer)
    print(answer)


if __name__ == '__main__':
    main()
