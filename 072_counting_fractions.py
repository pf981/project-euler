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

# 1: 0
# 2: 1/2
# 3: 1/2 1/3 2/3
# 4: 1/2 1/3 2/3 1/4 *2/4 3/4
# 5: 1/2 1/3 2/3 1/4 3/4 1/5 2/5 3/5 4/5
# 6L 1/2 1/3 2/3 1/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6

MAX_DENOMINATOR = 1000000

def main():
    answer = 0
    for denominator in range(1, MAX_DENOMINATOR + 1):
        if denominator % 1000 == 0:
            print(denominator)
        for numerator in range(1, denominator):
            if fractions.gcd(numerator, denominator) == 1:
                answer += 1

    print(answer)

if __name__ == '__main__':
    main()