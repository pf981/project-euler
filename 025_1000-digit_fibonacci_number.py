import itertools
from helpers import helpers


def main():
    # print(list(itertools.islice(helpers.fibonacci(), 10)))
    answer = next((i + 1 for i, val in enumerate(helpers.fibonacci()) if len(str(val)) >= 1000))

    print(answer)

if __name__ == '__main__':
  main()
