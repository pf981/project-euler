from functools import reduce
from operator import mul

def product(num_list):
    """
    Returns the product of each element of the list, similar to sum(num_list)
    """
    answer = reduce(mul, num_list, 1)

def prime_factors_range(start, stop=None):
    # parse input options
    if not stop:
        stop = start
        start = 0
    else:
        start = start
        stop = stop

    factors = {}
    for key in range(start, stop):
        factors[key] = prime_factors(key)

    return factors

# Taken from http://stackoverflow.com/questions/18833759/python-prime-number-checker
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
