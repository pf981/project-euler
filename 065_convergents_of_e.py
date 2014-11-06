# This is rubbish. This is just kept for reference purposes. My successful
# attempt is in 065_convergents_of_e2.py
# 2 = 2
# 2 + 1/1 = 3
# 2 + 1/(1 + 1/2) = 8/3
# 2 + 1/(1 + 1/(2 + 1/1)) = 11/4
# 2 + 1/(1 + 1/(2 + 1/(1 + 1/1))) = 11/4

# --- New sequence ---
# 1/1 = 1
# 1/(1 + 1/2) = 2/3
# 1/(1 + 1/(2 + 1/1)) = 3/4
# 1/(1 + 1/(2 + 1/(1 + 1/1))) = 5/7

# Need to work backwards?

from fractions import Fraction

def compute_denominators(max_terms):
    """
    Returns a list of Fractions which represent the denominators in the sequence.
    For example, denominator[1] = 2, so the first iteration is 1 + 1/2
    denominator[2] = 2.5, so the second iteration is 1 + 1/2.5
    """
    # This is the list 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...
    # from [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]
    continued_fractions = [1]*max_terms
    continued_fractions[1] = 2
    for i in range(4, max_terms, 3):
        print('!',i)
        continued_fractions[i] = continued_fractions[i-3] + 2

    sequence = {}
    sequence[0] = Fraction(1)
    sequence[1] = Fraction(1, 1 + Fraction(1, 2))

    for i in range(2, max_terms):
        sequence[i] = sequence[i-2] + Fraction(1, continued_fractions[i-1] + Fraction(1, continued_fractions[i]))

    return sequence

def compute_nth_term(n, denominator):
    """
    Returns the nth iteration of the sequence
    """
    return 1 + Fraction(1, denominator[n])

def main():


    denominators = compute_denominators(20)
    print(denominators)
    # Expected 1, 3/2, 4/3, 7/5

    # denominator = compute_denominators(1000)
    # terms = []

    # # For each term from 1 to 1000
    # for i in range(1, 1001):
    #     # Compute the value of the term and stor it in the terms list
    #     terms.append(compute_nth_term(i, denominator))

    # # The answer is the number terms whose numerator is larger than the denominator
    # answer = sum(1
    #              for fract in terms
    #              if len(str(fract.numerator)) > len(str(fract.denominator)))

    # print(answer)


if __name__ == '__main__':
    main()
