# This is essentially a brute force approach. It takes too long to run so a
# more efficient algorithm is used in 071_ordered_fractions2.py
from fractions import Fraction

MAX_DENOMINATOR = 1000000

def main():
    # Generate all the fractions and put them in order
    fractions = sorted(list(set(Fraction(n, d)
                                for d in range(1, MAX_DENOMINATOR + 1)
                                for n in range(1, d))))

    # Find the one to the left of 3/7
    answer = next(fractions[i-1]
                  for i, val in enumerate(fractions)
                  if val == Fraction(3, 7))

    print(answer)

if __name__ == '__main__':
    main()