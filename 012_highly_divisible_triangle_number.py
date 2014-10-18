import itertools
from helpers import helpers

def triangle_numbers():
    triangle_num = 0
    for i in range(1, 100):
        triangle_num += i
        yield triangle_num

def main():
    for triangle_num in triangle_numbers():
        if len(helpers.factors(triangle_num)) > 5:
            answer = triangle_num
            break

    print(answer)


if __name__ == '__main__':
  main()
