from helpers import helpers

PRIMES = helpers.get_million_primes()

def is_double_truncated(prime):
    dividend = 10
    while dividend < prime:
        if prime % dividend not in PRIMES or prime // dividend not in PRIMES:
            return False
        dividend *= 10
    return True

def main():
    truncatable_primes = []

    # For each prime > 10
    for p in PRIMES[4:]:
        if is_double_truncated(p):
            truncatable_primes.append(p)
            print(p)
            if len(truncatable_primes) == 11:
                break

    print(truncatable_primes)
    answer = sum(truncatable_primes)
    print(answer)

if __name__ == '__main__':
    main()
