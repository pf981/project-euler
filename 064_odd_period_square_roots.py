# This algorithm keeps track of all a_i in x = [a_0; a_1, a_2 ...]. A slightly
# more efficient implementation that just keeps track of the number of a_i's
# but doesn't store them in a list can be found in
# 064_odd_period_square_roots2.py
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
    odd_periods_count = 0

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
        if (x == int(x)):
            continue

        # a_0 = floor(x)
        a = [x.to_integral_exact(rounding=decimal.ROUND_FLOOR)]

        # r_0 = x
        r = [x]

        # x is periodic about a_0 and 2*a_0
        while a[-1] != 2 * a[0]:
            # I was getting the incorrect result as my decimal precision was
            # not sufficient. To detect when it was insufficient, I used the
            # below check. It is based off:
            #     http://mathworld.wolfram.com/ContinuedFraction.html
            # Statement 41 in the mathworld link states that 0 < a_n < 2*sqrt(n) for all n<k
            # The check below checks if this condition has been violated. If
            # it has, it is certainly due to rounding errors
            if a[-1] > 2*x:
                print("ERROR: a_n > 2sqrt(n). Increase decimal precision to resolve this issue.", n, x, a[-1], a[0])

            # r_n = 1 / (r_{n-1} - a_{n-1})
            r.append(1 / (r[-1] - a[-1]))

            # a_n = floor(r_n)
            a.append(r[-1].to_integral_exact(rounding=decimal.ROUND_FLOOR))
        # print("sqrt({0}) [{1}; {2}]".format(n, a[0], tuple(a[1:])))
        print("sqrt", n)

        # Note that the periodic elements are a[1:]. a[0] is the first value
        # that is not part of the period
        # If the period is odd
        if len(a[1:]) % 2 == 1:
            odd_periods_count += 1
    return odd_periods_count

def main():
    answer = total_odd_periods()
    print(answer)

if __name__ == '__main__':
    main()