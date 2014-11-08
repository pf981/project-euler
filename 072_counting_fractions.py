import sympy

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
MAX_DENOMINATOR = 8

def extra_fractions_in_this_denominator(denominator):
        extra_fractions = denominator - 1

        # FIXME: This is excluding things multiple times
        for divisor in sympy.ntheory.primefactors(denominator):
            extra_fractions -= denominator // divisor - 1

        return extra_fractions

def main():
    answer = 0
    for denominator in range(2, MAX_DENOMINATOR + 1):
        answer += extra_fractions_in_this_denominator(denominator)

        if denominator % 1000 == 0:
            print(denominator)

    print(answer)

if __name__ == '__main__':
    main()
