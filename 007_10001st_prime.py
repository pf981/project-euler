# All primes > 3 are in the form 6k +/- 1
from helpers import primes

PRIME_N = 10001

def main():
    prime_list = [2, 3]

    k = 1
    while len(prime_list) < PRIME_N:
        if primes.is_prime(6 * k - 1):
            prime_list.append(6 * k - 1)
        if primes.is_prime(6 * k + 1):
            prime_list.append(6 * k + 1)
        k += 1

    answer = prime_list[PRIME_N - 1]
    print(answer)


if __name__ == '__main__':
  main()
