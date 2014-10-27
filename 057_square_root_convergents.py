from fractions import Fraction

# def denom(terms):
#     if terms == 0:
#         return 2

#     return 2 + 1/denom(terms-1)

# def sqrt2_approximation(terms):
#     return 1 + 1 /(denom(terms))

def compute_denominators(max_terms):
    denominator = {}
    denominator[1] = Fraction(2)

    for i in range(2, max_terms + 1):
        denominator[i] = 2 + 1/denominator[i-1]

    return denominator

# def compute_denominators(max_terms):
#     denominator = {}
#     denominator[1] = 2

#     for i in range(2, max_terms + 1):
#         denominator[i] = 2 + 1/denominator[i-1]

#     return denominator

# def sqrt2_approximation(terms):
#     # denominator[1] == 1.5 means the first denominator is 1.5
#     denominator = {}
#     denominator[1] = 2

#     for i in range(2, terms + 1):
#         denominator[i] = 2 + 1/denominator[i-1]

#     print(denominator)

#     return 1 + 1/denominator[terms]


def compute_nth_term(n, denominator):
    return Fraction(1, 1) + Fraction(1, denominator[n])

def main():
    denominator = compute_denominators(1000)
    terms = []

    for i in range(1, 1001):
        # terms.append(Fraction(1 + 1/denominator[i]))
        terms.append(compute_nth_term(i, denominator))

    answer = sum(1
                 for fract in terms
                 if len(str(fract.numerator)) > len(str(fract.denominator)))


    # print(sqrt2_approximation(4))
    # print(sqrt2_approximation(0))
    # print(sqrt2_approximation(1))
    # print(sqrt2_approximation(2))
    # print(sqrt2_approximation(3))
    # print(sqrt2_approximation(4))
    # result = 1
    # for _ in range(100):
    #     result
    # fractions.append(cur + 1/2)
    # cur += 1/(2 + 1/2)



    print(answer)


if __name__ == '__main__':
    main()
