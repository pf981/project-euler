import itertools
import math
from helpers import helpers

TERM_TO_FIND = 7

def main():
    # print(list(itertools.islice(helpers.fibonacci(), 10)))
#    answer = next((i for i, val in enumerate(helpers.fibonacci()) if len(str(x)) >= 1000))
#    answer = next((val for i, val in enumerate(helpers.fibonacci()) if i == TERM_TO_FIND - 1))
    answer = next((i + 1 for i, val in enumerate(helpers.fibonacci()) if len(str(val)) >= 1000))
#    answer = next((i + 1 for i, val in enumerate(helpers.fibonacci()) if val == 89))

    print(answer)

if __name__ == '__main__':
  main()
