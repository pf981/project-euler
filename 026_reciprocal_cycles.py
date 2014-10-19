import itertools
    # x = 0.(123)
    # 1000x = 123.(123)
    # 999x = 123
    # x = 123/999

    # x = 0.(142857)
    # 1000000x = 142857.(142857)
    # 999999x = 142857
    # x = 142857/999999

    # find n for the biggest y such that n % (10**y - 1) == 0
    # Here, y is known as the order of n
# NO!!!
# it is:
# order such that (10**order - 1) % n == 0

def recurring_length(n):
    # Find exponent such that n % (10**exponent - 1) == 0
#    order = 0
    for order in range(1, n):
        # Can optimize this exponentiation by keeping track of old exponents
        print(n, order, (10**order - 1 ) % 7)
        if (10**order - 1) % n == 0:
#            print("@@", order)
            return order
    return 0
    # This is a bad way of doing it - the ones that don't recur will take the longest

def main():
    # Only odd numbers can be recurring
    for d in range(7, 1000, 2):
        pass
    answer = recurring_length(7)
    print(answer)

if __name__ == '__main__':
    main()
