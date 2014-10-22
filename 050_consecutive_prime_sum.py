from helpers import helpers

UPPER_BOUND = 1000000
PRIMES = list(helpers.primes_to(UPPER_BOUND))
PRIMES_SET = frozenset(PRIMES)

def most_consecutive_prime_sum():
    print(PRIMES)
    print()

    # Find the smallest upper bound for the length of the sublist
    max_length = 0
    list_sum = 0
    while list_sum < 1000000:
        max_length += 1
        list_sum += PRIMES[max_length]

    # For each possible length, from largest to smallest
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
                print(length)
                break

            print()
            if list_sum in PRIMES_SET:
                print("@", list_sum, sum(PRIMES[start:start+length]), PRIMES[start:start+length])
                return(list_sum)


def main():
    answer = most_consecutive_prime_sum()
    print(answer)

if __name__ == '__main__':
    main()
