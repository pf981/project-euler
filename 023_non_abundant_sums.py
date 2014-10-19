from helpers import helpers

def is_abundant(n):
    # - n is to remove n as a factor
    return sum(helpers.factors(n)) - n > n

def get_abundant_numbers():
    return [n for n in range(12, 28124) if is_abundant(n)]

def main():
    abundant_numbers = get_abundant_numbers()

    sums_of_abundant_pairs = set()

    # Compute all sums of abundant numbers
    for abundant1 in abundant_numbers:
        for abundant2 in abundant_numbers:
            sum_of_abundant = abundant1 + abundant2

            # If the sum is out of the range we are checking
            if sum_of_abundant > 28123:
                break

            # Add the sum to the set of sums
            sums_of_abundant_pairs.add(sum_of_abundant)

    # Get the inverse of the set within the range
    not_sum_of_abundants = set(range(1, 28123)) - sums_of_abundant_pairs
    answer = sum(not_sum_of_abundants)
    print(answer)

if __name__ == '__main__':
  main()
