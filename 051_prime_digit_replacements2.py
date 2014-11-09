# After analysing the problem, we need to look for a prime candidate that has:
#  - 6 digits
#  - Exactly 3 repeating digits
#
# Once we have our candidate, we just replace the repeated digit with any
# other number and count how many primes this yields
import sympy

# Generate all six-digit primes
DIGITS = 6
PRIMES = list(sympy.sieve.primerange(10**(DIGITS-1), 10**DIGITS))

def compute_family(prime_str, to_replace):
    family = sum(1
                 for digit in '0123456789'
                 if int(prime_str.replace(to_replace, digit)) in PRIMES)
    return family

def compute_eight_prime():
    for prime in PRIMES:
        candidate = str(prime)

        # If it has a digit which is repeated 3 times that is 0, 1 or 2
        # then we should check it's family. If it has a family of 8
        if any(candidate.count(repeated_digit) == 3 and compute_family(candidate, repeated_digit) == 8
               for repeated_digit in '0123456789'):
            return prime

def main():
    answer = compute_eight_prime()
    print(answer)

if __name__ == '__main__':
    main()