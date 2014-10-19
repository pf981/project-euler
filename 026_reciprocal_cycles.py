# Thoughts:
# x = 0.(123)
# 1000x = 123.(123)
# 999x = 123
# x = 123/999
#
# x = 0.(142857)
# 1000000x = 142857.(142857)
# 999999x = 142857
# x = 142857/999999
#
# So 1/7 = something / 999999
# So 999999 mod 7 == 0 and the length of the cycle is the number of digits in 999999. Ie 6.
# We'll call this length "order"
# order is such that (10**order - 1) % n == 0
import itertools

def recurring_length(n):
    # Find exponent such that (10**exponent - 1) % n == 0
    for order in range(1, n):
        # Could optimize this exponentiation by keeping track of old exponents
        if (10**order - 1) % n == 0:
            return order
    return 0

def main():
    answer = max((d for d in range(7, 1000, 2)),
                 key=lambda x: recurring_length(x))
    print(answer)

if __name__ == '__main__':
    main()
