from fractions import Fraction

MAX_DENOMINATOR = 1000000

def main():
    target = Fraction(3, 7)
    candidate_denominators = (d for d in range(1, MAX_DENOMINATOR + 1) if d != target.denominator)

    min_distance = 99
    for candidate_denominator in candidate_denominators:
        numerator = int(candidate_denominator * target)
        candidate_fraction = Fraction(numerator, candidate_denominator)

        if candidate_fraction >= target:
            candidate_fraction = Fraction(numerator - 1, candidate_denominator)

        distance = target - candidate_fraction

        if distance < min_distance:
            min_distance = distance
            answer = candidate_fraction

    print(answer)

if __name__ == '__main__':
    main()