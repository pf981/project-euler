# This question is essentially asking for the sum of totients <= 1000000. To
# do this, I use a totient sieve
MAX_DENOMINATOR = 1000000

def count_fractions():
    # See http://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently

    # phi is the list of totients
    phi = list(range(MAX_DENOMINATOR+1))

    for i in range(2, MAX_DENOMINATOR+1):
        if phi[i] == i:
            for j in range(i, MAX_DENOMINATOR+1, i):
                phi[j] -= phi[j] // i

    print(list(range(MAX_DENOMINATOR+1)))
    print(phi)

    # Don't count the tot(1) == 1
    return sum(phi) - 1

def main():
    answer = count_fractions()
    print(answer)

if __name__ == '__main__':
    main()