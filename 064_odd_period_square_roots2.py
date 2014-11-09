import math
# http://mathworld.wolfram.com/ContinuedFraction.html
#     a_0 = floor(x)
#     r_0 = x
#     r_n = 1 / (r_{n-1} - a_{n-1})
#     a_n = floor(r_n)
# Where x = [a_0; a_1, a_2, a_3, ...]
#
# So for x = sqrt(24)
#     a_0 = floor(x) = 4
#     r_0 = x = sqrt(24)
#     r_1 = 1 / (r_0 - a_0) = 1/(sqrt(24) - 4)
#     a_1 = floor(r_1) = 1
#     etc.
#
# So the question is, how to (efficiently and difinitively) tell if it's
# periodic?  Well, we can see if r_i, a_i = r_k, a_k for i != k then it is
# periodic between i and k. But there is a better way. From the mathworld
# page:
#     The square root of a squarefree integer has a periodic continued
#     fraction of the form:
#         sqrt(n) = [a_0; (a_1, ..., a_n, 2a_0)]
# So, we know that it must be periodic between a_0 and a_k such that a_k =
# 2*a_0. That is, the period is k such that a_k = 2*a_0.
MAX_ROOT = 10000

def total_odd_periods():
    total_odd_periods = 0

    for n in range(2, MAX_ROOT+1):
        x = math.sqrt(n)

        # If it isn't an irrational square root, we aren't interested
        # Note that for all integers, a, sqrt(a) is either an integer or
        # irrational. So this means, every x that does not satisfy this if
        # condition must have an irrational root
        if (x == int(x)):
            continue

        # a_0 = floor(x)
        a_0 = math.floor(x)
        a_n = a_0

        # r_0 = x
        r_n = x

        period_length = 0
        # x is periodic about a_0 and 2*a_0
        while a_n != 2 * a_0:
            # r_n = 1 / (r_{n-1} - a_{n-1})
            r_n = 1 / (r_n - a_n)

            # a_n = floor(r_n)
            a_n = math.floor(r_n)

            period_length += 1
        # print("sqrt({0}) [{1}; {2}]".format(n, a_0_, tuple(a[1:])))
        # print("sqrt", n)

        # Note that the periodic elements are a[1:]. a[0] is the first value
        # that is not part of the period
        # If the period is odd
        if period_length % 2 == 1:
            total_odd_periods += 1

    return total_odd_periods

def main():
    answer = total_odd_periods()
    print(answer)

if __name__ == '__main__':
    main()