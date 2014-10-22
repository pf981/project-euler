from helpers import helpers

UPPER_BOUND = 1000000
PRIMES = list(helpers.primes_to(UPPER_BOUND))
PRIMES_SET = frozenset(PRIMES)

def most_consecutive_prime_sum():
    print(PRIMES)
    print()

    max_length = 0
    list_sum = 0
    while list_sum < 1000000:
        max_length += 1
        list_sum += PRIMES[max_length]

    # For each possible length, from largest to smallest
#    for length in reversed(range(1, len(PRIMES) + 1)):
    for length in reversed(range(1, max_length)):
    # while True:
    #     length = len(PRIMES)
    #     while sum(PRIMES[:length]) > 1000000:
    #         length -= 1

        for start in range(len(PRIMES) - length + 1):
            if start == 0:
                # list_sum is the sum from start to length of the primes
                list_sum = sum(PRIMES[:length])
            else:
                # Instead of recalculating the sum, subtract the first and add the last
                list_sum += PRIMES[start + length - 1]
                list_sum -= PRIMES[start-1]

            if list_sum > UPPER_BOUND:
                print(length)
                break
            print()
            if list_sum in PRIMES_SET:
                print("@", list_sum, sum(PRIMES[start:start+length]), PRIMES[start:start+length])
                return(list_sum)





    # print(PRIMES)
    # print()
    # # For each possible length, from largest to smallest
    # for length in reversed(range(1, len(PRIMES) + 1)):
    #     for start in range(len(PRIMES) - length + 1):
    #         if start == 0:
    #             # list_sum is the sum from start to length of the primes
    #             list_sum = sum(PRIMES[:length])
    #         else:
    #             # Instead of recalculating the sum, subtract the first and add the last
    #             list_sum += PRIMES[start + length - 1]
    #             list_sum -= PRIMES[start-1]

    #         if list_sum in PRIMES_SET:
    #             print("@", list_sum, sum(PRIMES[start:start+length]), PRIMES[start:start+length])
    #             return(list_sum)





    # print(PRIMES)
    # print()
    # # For each possible length, from largest to smallest
    # for length in reversed(range(1, len(PRIMES) + 1)):
    #     # Keep track of the sum
    #     list_sum = sum(PRIMES[:length])
    #     print(PRIMES[:length], list_sum)

    #     # Find each sublist of that length
    #     for start in range(len(PRIMES) - length + 1):
    #         print(start, length, list_sum)
    #         # FIXME: This is finding the wrong number (73 instead of 21. Says it has 7 sums)
    #         if list_sum in PRIMES_SET:
    #             # FIXME: This sum is not correct
    #             print(list_sum, sum(PRIMES[start:start+length]), PRIMES[start:start+length])
    #             return(list_sum)

    #         list_sum += PRIMES[start + length - 1]
    #         list_sum -= PRIMES[start]






        # To shift the list to the right, just subtract the first element and add the one after the last


    # # For each possible length, from largest to smallest
    # for length in reversed(range(len(PRIMES))):
    #     # Find each sublist of that length
    #     for sublist in helpers.all_fixed_length_sublists(PRIMES, length):
    #         list_sum = sum(sublist)
    #         if list_sum > UPPER_BOUND:
    #             continue
    #         if list_sum in PRIMES_SET:
    #             return list_sum


# def most_consecutive_prime_sum():
#     max_length = 0
#     most_consecutive_prime = None

#     for start in range(len(PRIMES)-1):
#         for end in reversed(range(start+2, len(PRIMES))):
#             # If it isn't composed of more consecutive primes
#             if len(PRIMES[start:end]) <= max_length:
#                 continue # Don't even try

#             prime_sum = sum(PRIMES[start:end])

#             if prime_sum in PRIMES_SET:
#                 max_length = len(PRIMES[start:end])
#                 print(prime_sum, PRIMES[start:end])
#                 most_consecutive_prime = prime_sum

#     return most_consecutive_prime

def main():
    answer = most_consecutive_prime_sum()
    print(answer)

if __name__ == '__main__':
    main()
