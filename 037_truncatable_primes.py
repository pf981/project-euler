from helpers import helpers

def get_truncations(num):
    string = str(num)

    # Left to right
    for i in reversed(range(1, len(string))):
        yield int(string[:i])

    # Right to left
    for i in reversed(range(1, len(string))):
        yield int(string[-i:])

def main():
    primes = helpers.get_million_primes()
    truncatable_primes = []

    # For each prime > 10
    for p in primes[4:]:
        if all(i in primes for i in get_truncations(p)):
            truncatable_primes.append(p)
            print(p)
            if len(truncatable_primes) == 11:
                break

    print(truncatable_primes)
    answer = sum(truncatable_primes)
    print(answer)

if __name__ == '__main__':
    main()
