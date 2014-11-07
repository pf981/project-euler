import itertools
import math

def get_chain_length(n, non_repeating_terms):
    for extra_terms in itertools.count(0):
        if n in non_repeating_terms:
            return non_repeating_terms[n] + extra_terms

        n = sum(math.factorial(int(digit)) for digit in str(n))


def main():
    non_repeating_terms = {}
    non_repeating_terms[169] = non_repeating_terms[363601] = non_repeating_terms[1454] = 3
    non_repeating_terms[871] = non_repeating_terms[45361] = 2
    non_repeating_terms[872] = non_repeating_terms[45362] = 2
    non_repeating_terms[145] = 1

    # for n in range(100):
    #     get_chain_length(n, non_repeating_terms)

    # print(non_repeating_terms)
    # print(get_chain_length(540, non_repeating_terms))

    answer = sum(1 for n in range(100) if get_chain_length(n, non_repeating_terms) == 60)
    print(answer)

if __name__ == '__main__':
    main()