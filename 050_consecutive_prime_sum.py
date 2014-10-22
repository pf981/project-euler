from helpers import helpers

UPPER_BOUND = 1000000
# Primes were stored as both a list and a set because lists are better for
# iterating over whereas sets are better for determining if an element is a
# member of that set. Both types were chosen as a significant amount of
# iterating and using the "in" keyword were common in this problem.
PRIMES = list(helpers.primes_to(UPPER_BOUND))
PRIMES_SET = frozenset(PRIMES)

def most_consecutive_prime_sum():
    # Find the smallest upper bound for the length of the sublist
    max_length = 0
    list_sum = 0
    while list_sum < 1000000:
        max_length += 1
        list_sum += PRIMES[max_length]

    # For each possible length, from largest to smallest
    # Note that if we started at len(PRIMES) instead of max_length it would
    # take infeasibly long
    for length in reversed(range(1, max_length)):
        for start in range(len(PRIMES) - length + 1):
            if start == 0:
                # list_sum is the sum from start to length of the primes
                list_sum = sum(PRIMES[:length])
            else:
                # Instead of recalculating the sum, subtract the first and add the last
                list_sum += PRIMES[start + length - 1]
                list_sum -= PRIMES[start-1]

            # If the sum is getting too big
            if list_sum > UPPER_BOUND:
                # Then the following sums will only be bigger, so break
                break

            # If the sum is a prime, it must be the prime with the biggest
            # sequence length
            if list_sum in PRIMES_SET:
                return(list_sum)


def main():
    answer = most_consecutive_prime_sum()
    print(answer)

if __name__ == '__main__':
    main()
