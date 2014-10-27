from fractions import Fraction

def compute_denominators(max_terms):
    """
    Returns a list of Fractions which represent the denominators in the sequence.
    For example, denominator[1] = 2, so the first iteration is 1 + 1/2
    denominator[2] = 2.5, so the second iteration is 1 + 1/2.5
    """
    denominator = {}
    denominator[1] = Fraction(2)

    for i in range(2, max_terms + 1):
        denominator[i] = 2 + 1/denominator[i-1]

    return denominator

def compute_nth_term(n, denominator):
    """
    Returns the nth iteration of the sequence
    """
    return 1 + Fraction(1, denominator[n])

def main():
    denominator = compute_denominators(1000)
    terms = []

    # For each term from 1 to 1000
    for i in range(1, 1001):
        # Compute the value of the term and stor it in the terms list
        terms.append(compute_nth_term(i, denominator))

    # The answer is the number terms whose numerator is larger than the denominator
    answer = sum(1
                 for fract in terms
                 if len(str(fract.numerator)) > len(str(fract.denominator)))

    print(answer)


if __name__ == '__main__':
    main()
