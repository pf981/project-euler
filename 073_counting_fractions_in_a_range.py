from fractions import Fraction

MAX_DENOMINATOR = 12000

def main():
    left = Fraction(1, 3)
    right = Fraction(1, 2)

    # Generate all the fractions and put them in order
    fractions = sorted(list(set(Fraction(n, d)
                                for d in range(1, MAX_DENOMINATOR + 1)
                                for n in range(1, d))))

    fractions_between = fractions[fractions.index(left)+1 : fractions.index(right)]
    answer = len(fractions_between)
    print(answer)

if __name__ == '__main__':
    main()