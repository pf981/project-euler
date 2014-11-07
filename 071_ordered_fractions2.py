# Instead of generating all fractions, it just looks at one fraction per
# denominator. The numerator is constructed such that the fraction forms the
# closest possible fraction to 3/7. The answer is just the fraction that is
# the closest to the target.
from fractions import Fraction

MAX_DENOMINATOR = 1000000

def main():
    target = Fraction(3, 7)

    min_distance = None
    for denominator in range(1, MAX_DENOMINATOR + 1):
        # 3/7 = x/d => x = d*3/7
        # By rounding down x, x/d will be the closest approximation to 3/7
        # that this denominator can provide
        numerator = int(denominator * target)
        fraction = Fraction(numerator, denominator)

        # We want the fraction to be to the left (smaller) than the target
        if fraction >= target:
            # By construction, this is guaranteed to make fraction < target
            fraction = Fraction(numerator - 1, denominator)

        distance = target - fraction

        if not min_distance or distance < min_distance:
            min_distance = distance
            answer = fraction

    print(answer)

if __name__ == '__main__':
    main()