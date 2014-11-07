# Instead of generating all fractions, it just looks at one fraction per
# denominator. The numerator is constructed such that the fraction forms the
# closest possible fraction to 1/2. The numerator is iterated down until the
# fraction passes 1/2. The answer is the count of how many numbers lay between
# 1/2 and 1/3
from fractions import Fraction

MAX_DENOMINATOR = 12000

def main():
    left = Fraction(1, 3)
    right = Fraction(1, 2)

    between_list = set()
    # answer = 0
    for denominator in range(1, MAX_DENOMINATOR + 1):
        # current_between_list = set()
        print(denominator)
        # 3/7 = x/d => x = d*3/7
        # By rounding down x, x/d will be the closest approximation to 3/7
        # that this denominator can provide
        numerator = int(denominator * right)
        fraction = Fraction(numerator, denominator)

        # We want the fraction to be to the left (smaller) than the right
        if fraction >= right:
            # By construction, this is guaranteed to make fraction < right
            numerator -= 1
            fraction = Fraction(numerator, denominator)

        while fraction > left:
            # between_list.append(fraction)
            # answer += 1
            # current_between_list.add(fraction)
            between_list.add(fraction)
            numerator -= 1
            fraction = Fraction(numerator, denominator)
        # answer += len(current_between_list)

    # print(between_list)
    answer = len(between_list)
    print(answer)

if __name__ == '__main__':
    main()