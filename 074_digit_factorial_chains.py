import itertools
import math

def get_chain_length(n, non_repeating_terms):
    cur_term = n
    prev_term = None

    for extra_terms in itertools.count(0):
        if cur_term in non_repeating_terms:
            non_repeating_terms[n] = non_repeating_terms[cur_term] + extra_terms
            return non_repeating_terms[n]

        prev_term = cur_term
        cur_term = sum(math.factorial(int(digit)) for digit in str(cur_term))

        if cur_term == prev_term:
            non_repeating_terms[n] = 1 + extra_terms
            return non_repeating_terms[n]



def main():
    non_repeating_terms = {}
    non_repeating_terms[169] = non_repeating_terms[363601] = non_repeating_terms[1454] = 3
    non_repeating_terms[871] = non_repeating_terms[45361] = 2
    non_repeating_terms[872] = non_repeating_terms[45362] = 2

    answer = sum(1 for n in range(1000000) if get_chain_length(n, non_repeating_terms) == 60)
    print(answer)

if __name__ == '__main__':
    main()