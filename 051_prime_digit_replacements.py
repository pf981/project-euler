from sympy import sieve

def main():
    digits = 1
    sieve.extend(10**digits)
    print(sieve)
    # cur_prime = sympy.nextprime(2)
    # while(True):
    #     primes.append(cur_prime)
    #     cur_prime = sympy.nextprime(cur_prime)


if __name__ == '__main__':
    main()