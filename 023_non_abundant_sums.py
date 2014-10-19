from helpers import helpers



def is_abundant(n):
    # - n is to remove n as a factor
    return sum(helpers.factors(n)) - n > n


def get_abundant_numbers():
    # FIXME: Not sure of this upper bound
    return [n for n in range(12, 28124) if is_abundant(n)]

# HACK


def is_sum_of_abundant(n):
    for abundant1 in abundant_numbers:
#        print(abundant1)
        if abundant1 >= n:
            break

        # If n can be expressed as abundant1 + abundant2
        if n - abundant1 in abundant_numbers:
            return True
    return False

def main():
    abundant_numbers = get_abundant_numbers()

    sums_of_abundant_pairs = set()

    # Compute all sums of abundant numbers
    for abundant1 in abundant_numbers:
        for abundant2 in abundant_numbers:
            sum_of_abundant = abundant1 + abundant2
            if sum_of_abundant > 28123:
                break
            sums_of_abundant_pairs.add(sum_of_abundant)

    not_sum_of_abundants = set(range(1, 28123)) - sums_of_abundant_pairs
    answer = sum(not_sum_of_abundants)
    print(answer)

#            print(sum_of_abundant)

#    print(sums_of_abundant_pairs)

#    print(get_abundant_numbers())
#    not_sum_of_abundants = [n for n in range(1, 28123) if not is_sum_of_abundant(n)]
#    print(is_sum_of_abundant(24))
#    not_sum_of_abundants = [n for n in range(1, 30) if not is_sum_of_abundant(n)]

#    print(not_sum_of_abundants)
#    answer = sum(not_sum_of_abundants)
#    print(answer)
#    abundant_numbers = get_abundant_numbers()
#    print(helpers.factors(28))
#    print(is_abundant(28))
#    print(is_abundant(12))
#    answer = 0
#    print(answer)
#    print(abundant_numbers)

if __name__ == '__main__':
  main()
