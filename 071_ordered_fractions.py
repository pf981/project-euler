from fractions import Fraction

MAX_DENOMINATOR = 1000000

def main():
    fractions = sorted(list(set(Fraction(n, d)
                                for d in range(1, MAX_DENOMINATOR + 1)
                                for n in range(1, d))))

    answer = next(fractions[i-1]
                  for i, val in enumerate(fractions)
                  if val == Fraction(3, 7))

    print(answer)

if __name__ == '__main__':
    main()