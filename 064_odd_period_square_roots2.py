import decimal
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

    # Note that if we use math.sqrt instead of Decimal.sqrt, we get rounding
    # errors that result in the incorrect result. I tried sympy (symbolic
    # sqrt), but that was too slow. We don't need the calculation to be exact,
    # but we need it to be better than what math.sqrt was giving. Even 100
    # decimal places resulted in errors. However, 100 decimal places gave the
    # correct answer. Some potential significant rounding errors are detected
    # in an if statement further down.
    decimal.getcontext().prec = 1000

    for n in range(2, MAX_ROOT+1):
        x = decimal.Decimal(n).sqrt()

        # If it isn't an irrational square root, we aren't interested
        # Note that for all integers, a, sqrt(a) is either an integer or
        # irrational. So this means, every x that does not satisfy this if
        # condition must have an irrational root
        if (x == int(x)):
            continue

        # a_0 = floor(x)
        a_0 = x.to_integral_exact(rounding=decimal.ROUND_FLOOR)
        a_n = a_0

        # r_0 = x
        r_n = x

        period_length = 0
        # x is periodic about a_0 and 2*a_0
        while a_n != 2 * a_0:
            # I was getting the incorrect result as my decimal precision was
            # not sufficient. To detect when it was insufficient, I used the
            # below check. It is based off:
            #     http://mathworld.wolfram.com/ContinuedFraction.html
            # Statement 41 in the mathworld link states that 0 < a_n < 2*sqrt(n) for all n<k
            # The check below checks if this condition has been violated. If
            # it has, it is certainly due to rounding errors
            if a_n > 2*x:
                print("ERROR: a_n > 2sqrt(n). Increase decimal precision to resolve this issue.", n, x, a_n, a_0)

            # r_n = 1 / (r_{n-1} - a_{n-1})
            r_n = 1 / (r_n - a_n)

            # a_n = floor(r_n)
            a_n = r_n.to_integral_exact(rounding=decimal.ROUND_FLOOR)

            period_length += 1
        # This print is just so we can keep track of the program's progress
        print("sqrt", n)

        # If the period is odd
        if period_length % 2 == 1:
            total_odd_periods += 1

    return total_odd_periods

def main():
    answer = total_odd_periods()
    print(answer)

if __name__ == '__main__':
    main()