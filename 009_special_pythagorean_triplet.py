from functools import reduce
from operator import mul

# a + b + c = RHS
RHS = 1000

def is_triplet(a, b, c):
    return a*a + b*b == c*c

def find_triplet():
    for a in range(1, RHS):
        for b in range(1, RHS - a):
            c = 1000 - a - b
            if is_triplet(a, b, c):
                return (a, b, c)


def main():
    answer = reduce(mul, find_triplet(), 1)
    print(answer)


if __name__ == '__main__':
  main()
