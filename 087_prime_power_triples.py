import sympy

MAX_NUM = 50000000

def main():
    print("Generating {0} primes.".format(MAX_NUM))
    primes = list(sympy.sieve.primerange(2, MAX_NUM**(1/2)))
    squares = [prime**2 for prime in primes]
    cubes = [prime**3 for prime in primes if prime**3 < MAX_NUM]
    fourths = [prime**4 for prime in primes if prime**4 < MAX_NUM]
    print("Done.")
    # print(squares)
    # print(cubes)
    # print(fourths)
    # sums = [square + cube + fourth
    #         for square in squares
    #         for cube in cubes
    #         for fourth in fourths
    #         if square + cube + fourth < MAX_NUM]
    # print(sums)
    sums = set()
    for square in squares:
        print(square)
        for cube in cubes:
            for fourth in fourths:
                prime_power_triple = square + cube + fourth
                if prime_power_triple < MAX_NUM:
                    sums.add(prime_power_triple)

    answer = len(sums)
    print(answer)

if __name__ == '__main__':
    main()