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
import sympy
import fractions

# 1:
# 2: 1/2
# 3: 1/2 1/3 2/3
# 4: 1/2 1/3 2/3 1/4 *2/4 3/4
# 5: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5
# 6: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6
# 7: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6 1/7 2/7 3/7 4/7 5/7 6/7
# 8: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6 1/7 2/7 3/7 4/7 5/7 6/7 1/8 *2/8 3/8 *4/8 5/8 *6/8 7/8
# 9: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6 1/7 2/7 3/7 4/7 5/7 6/7 1/8 *2/8 3/8 *4/8 5/8 *6/8 7/8 1/9 2/9 *3/9 4/9 5/9 *6/9 7/9 8/9


# MAX_DENOMINATOR = 1000000
MAX_DENOMINATOR = 9
# PRIMES = set(sympy.sieve.primerange(2, MAX_DENOMINATOR))

# Maybe I just want prime factors
def non_trivial_divisors(n):
    # All the divisors except 1 and n
#    return sympy.ntheory.divisors(n)[1:-1]
    return sympy.ntheory.primefactors(n)

def main():
    answer = 0
    for denominator in range(2, MAX_DENOMINATOR + 1):

        answer = 0 # FIXME: REMOVE
        answer += denominator - 1

        # This is excluding things multiple times
        for divisor in non_trivial_divisors(denominator):
            answer -= denominator // divisor - 1
        # for divisor in non_trivial_divisors(denominator):
        #     answer -= denominator // divisor - 1

        print(denominator, answer)
        # print(denominator, denominator - len(sympy.ntheory.divisors(denominator)) + 1)
        # print(sympy.ntheory.divisors(denominator))
        # print(non_trivial_divisors(denominator))
        # print()
        # answer += denominator - len(sympy.ntheory.divisors(denominator)) + 1
        # print(denominator, denominator - len(sympy.ntheory.divisors(denominator)) + 1)
        # print(sympy.ntheory.divisors(denominator))
        # print(non_trivial_divisors(denominator))
        # print()
        # FIXME: Not divisors, common
        # if denominator in PRIMES:
        #     answer += denominator - 1
        # else:

        if denominator % 1000 == 0:
            print(denominator)
        # for numerator in range(1, denominator):
        #     if fractions.gcd(numerator, denominator) == 1:
        #         answer += 1

    print(answer)

if __name__ == '__main__':
    main()