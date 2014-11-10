import sympy

MAX_NUM = 50

def main():
    primes = list(sympy.sieve.primerange(2, MAX_NUM**(1/2)))
    squares = [prime**2 for prime in primes]
    cubes = [prime**3 for prime in primes]
    fourths = [prime**4 for prime in primes]
    print(squares)
    print(cubes)
    print(fourths)
    sums = [square + cube + fourth
            for square in squares
            for cube in cubes
            for fourth in fourths
            if square + cube + fourth < MAX_NUM]
    print(sums)
    answer = len(sums)
    print(answer)

if __name__ == '__main__':
    main()