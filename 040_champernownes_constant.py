from helpers import helpers

def main():
    digits = ''.join([str(x) for x in range(1, 1000000)])

    # nths = [1, 10 ,..., 1000000]
    nths = [10**n for n in range(7)]

    # Answer is the product of d_n
    answer = helpers.product(int(digits[nth - 1]) for nth in nths)

    print(answer)

if __name__ == '__main__':
    main()
