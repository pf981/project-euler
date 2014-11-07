# I started this problem by using fractions.Fraction to simplify each fraction
# and put the in a set to remove duplicates. However, this method took over 6
# minutes to run. By simply checking if the gcd is 1 and only accepting
# simplified fractions, fractions.Fraction was avoided alltogether and the
# runtime was reduced to 14s
#
# Instead of generating all fractions, it just looks at one fraction per
# denominator. The numerator is constructed such that the fraction forms the
# closest possible fraction to 1/2. The numerator is iterated down until the
# fraction passes 1/2. The answer is the count of how many numbers lay between
# 1/2 and 1/3
# from fractions import Fraction
import fractions

MAX_DENOMINATOR = 12000

def main():
    left = 1/3
    right = 1/2

    answer = 0
    for denominator in range(1, MAX_DENOMINATOR + 1):
        # 3/7 = x/d => x = d*3/7
        # By rounding down x, x/d will be the closest approximation to 3/7
        # that this denominator can provide
        numerator = int(denominator * right)

        # We want the fraction to be to the left (smaller) than the right
        if numerator/denominator >= right:
            # By construction, this is guaranteed to make fraction < right
            numerator -= 1

        while numerator/denominator > left:
            if fractions.gcd(numerator, denominator) == 1:
                answer += 1

            numerator -= 1

    print(answer)

if __name__ == '__main__':
    main()