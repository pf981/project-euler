# The totient function is tot such that
#     tot(n) = n * product (1 - 1/p)
# Where p are all the prime divisors of n. So,
#     n/tot(n) = 1 / product (1 - 1/p)
#
# Therefore, if we must maximise n/tot(n) we must the product. As tot(n)
# represents the number of prime divisors of n, we must maximise the number of
# prime divisors of n. To do this, we must simply multiply every prime number,
# starting from 2, until just before we surpass 1000000.
import sympy

MAX_N = 1000000
MAX_PRIMES = 300
PRIMES = sympy.sieve.primerange(2, MAX_PRIMES)

def main():
    answer = 1
    for prime in PRIMES:
        if answer * prime > MAX_N:
            break

        answer *= prime

    print(answer)

# yasnippit: type "ifmain" then tab to complete
if __name__ == '__main__':
    main()