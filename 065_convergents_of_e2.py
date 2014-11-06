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
from fractions import Fraction

def compute_continued_fractions(max_fractions):
    """
    Returns the list 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...
    from [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]
    """
    continued_fractions = [1] * max_fractions
    continued_fractions[1] = 2

    for i in range(4, max_fractions, 3):
        continued_fractions[i] = continued_fractions[i-3] + 2

    return continued_fractions

def compute_nth_term(n, continued_fractions):
    """
    Returns the nth iteration of the sequence
    """
    if n == 1:
        return 2

    n = n-2

    denominator = continued_fractions[n]
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
