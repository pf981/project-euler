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
#     r_2 = 1 / (r_1 - a_1) = 1/
#
# So the question is, how to (efficiently and difinitively) tell if it's periodic?
# Well, we can see if r_i, a_i = r_k, a_k for i != k then it is periodic between i and k.
#
# From the mathworld page:
#     The square root of a squarefree integer has a periodic continued fraction of the form
#         sqrt(n) = [a_0; (a_1, ..., a_n, 2a_0)]
# So, we know that it must be periodic between a_0 and a_k such that a_k = 2a_0
MAX_ROOT = 13

def main():
    for n in range(2, MAX_ROOT+1):
        x = math.sqrt(n)

        # If it isn't an irrational square root, we aren't interested
        if (x == int(x)):
            continue

        # a_0 = floor(x)
        a = [math.floor(x)]

        # r_0 = x
        r = [x]
        # for _ in range(6):
        # x is periodic about a_0 and 2*a_0
        while a[-1] != 2 * a[0]:
            # r_n = 1 / (r_{n-1} - a_{n-1})
            r.append(1 / (r[-1] - a[-1]))

            # a_n = floor(r_n)
            a.append(math.floor(r[-1]))
        print("sqrt({0}) [{1}; {2}]".format(n, a[0], tuple(a[1:])))

if __name__ == '__main__':
    main()