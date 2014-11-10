import sympy

MAX_NUM = 50000000

def main():
    primes = list(sympy.sieve.primerange(2, MAX_NUM**(1/2)))
    squares = [prime**2 for prime in primes]
    cubes = [prime**3 for prime in primes if prime**3 < MAX_NUM]
    fourths = [prime**4 for prime in primes if prime**4 < MAX_NUM]

    sums = set()

    # For all combinations of square prime, cube prime and fourth prime power
    for square in squares:
        for cube in cubes:
            for fourth in fourths:
                # Compute the sum
                prime_power_triple = square + cube + fourth

                # If the sum is within the range we are looking
                if prime_power_triple < MAX_NUM:
                    # Store it and remove duplicates
                    sums.add(prime_power_triple)

    answer = len(sums)
    print(answer)

if __name__ == '__main__':
    main()