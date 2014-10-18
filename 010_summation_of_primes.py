from helpers import primes

LIMIT = 2000000

def main():
    primes_below = primes.Sieve(LIMIT).listPrimes()
    answer = sum(primes_below)
    print(answer)


if __name__ == '__main__':
  main()
