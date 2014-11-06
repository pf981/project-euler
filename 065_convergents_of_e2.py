# 2 = 2
# 2 + 1/1 = 3
# 2 + 1/(1 + 1/2) = 8/3
# 2 + 1/(1 + 1/(2 + 1/1)) = 11/4
# 2 + 1/(1 + 1/(2 + 1/(1 + 1/1))) = 11/4
from fractions import Fraction

def compute_continued_fractions(max_fractions):
    """
    Returns the list 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...
    """
    # Create a list of ones
    continued_fractions = [1] * max_fractions

    # Set the non-one values
    continued_fractions[1] = 2
    for i in range(4, max_fractions, 3):
        continued_fractions[i] = continued_fractions[i-3] + 2

    return continued_fractions

# This function computes the "deepest" denominator first and works its way up
# to get the answer
#
# For example, if we wanted to compute the 5th term
# value_5 = 2 + 1/(1 + 1/(2 + 1/(1 + 1/1))) = 19/7; we compute
#                                1 + 1/1    = 2    = denominator
#                         2 + 1/denominator = 3/2  = denominator
#                  1 + 1/denominator        = 5/7  = denominator
#           2 + 1/denominator               = 19/7 = value_5
def compute_nth_term(n, continued_fractions):
    """
    Returns the nth iteration of the sequence
    """
    if n == 1:
        return 2

    # This is just to align n with our continued_fractions list indices
    n = n-2

    # Compute the last denominator
    denominator = continued_fractions[n]

    # Iterate through and compute "shallower" denominators
    for i in reversed(range(n)):
        denominator = continued_fractions[i] + Fraction(1, denominator)

    return 2 + Fraction(1, denominator)

def main():
    continued_fractions = compute_continued_fractions(100)
    nth_term = compute_nth_term(100, continued_fractions)
    answer = sum(int(n) for n in str(nth_term.numerator))
    print(answer)

if __name__ == '__main__':
    main()
