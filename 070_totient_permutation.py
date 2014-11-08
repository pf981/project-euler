import sys

UPPER_BOUND = 100

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def tot(n):
    pass

def main():
    answer = None
    best_ratio = None

    for n in range(UPPER_BOUND + 1):
        totient = tot(n)
        if is_permutation(n, totient):
            if not best_ratio or n / totient < best_ratio:
                answer = n
                best_ratio = n / totient

    print(answer)

if __name__ == '__main__':
    main()