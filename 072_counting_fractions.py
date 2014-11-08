# The number of extra fractions each denominator gives (that wasn't provided
# by the previous denominators) is equal to d-1 if d is prime. If d is not
# prime, it is equal to d - 1 - numbers_share_factors_with_d_less_than_d.
#
# The graph below shows the maximum denominator on the left and a list of all
# the possible fractions that can be made with denominators <= d. An asterisk
# denotes that this fraction is not simplified and should be excluded
#
# 1:
# 2: 1/2
# 3: 1/2 1/3 2/3
# 4: 1/2 1/3 2/3 1/4 *2/4 3/4
# 5: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5
# 6: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6
# 7: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6 1/7 2/7 3/7 4/7 5/7 6/7
# 8: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6 1/7 2/7 3/7 4/7 5/7 6/7 1/8 *2/8 3/8 *4/8 5/8 *6/8 7/8
# 9: 1/2 1/3 2/3 1/4 *2/4 3/4 1/5 2/5 3/5 4/5 1/6 *2/6 *3/6 *4/6 5/6 1/7 2/7 3/7 4/7 5/7 6/7 1/8 *2/8 3/8 *4/8 5/8 *6/8 7/8 1/9 2/9 *3/9 4/9 5/9 *6/9 7/9 8/9
# ...
# 12: ... 1/12 *2/12 *3/12 *4/12 5/12 *6/12 7/12 *8/12 *9/12 *10/12 11/12
import sympy

MAX_DENOMINATOR = 1000000

def extra_fractions_in_this_denominator(denominator):
        # This is the set of numerators which do not form simplified fractions with the denominator
        excluded_numerators = set()

        #  For each divisor
        for divisor in sympy.ntheory.primefactors(denominator):
            # Exclude all numerator multiples of that divisor
            numerator = divisor
            while numerator < denominator:
                if numerator not in excluded_numerators:
                    excluded_numerators.add(numerator)
                numerator += divisor

        # All the possible fractions
        extra_fractions = denominator - 1

        # Minus all the invalid fractions
        extra_fractions -= len(excluded_numerators)

        return extra_fractions

def main():
    answer = 0
    for denominator in range(2, MAX_DENOMINATOR + 1):
        answer += extra_fractions_in_this_denominator(denominator)

        # This is so we can see the progress of the solution
        if denominator % 1000 == 0:
            print(denominator)

    print(answer)

if __name__ == '__main__':
    main()
