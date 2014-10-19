import itertools
import re
from functools import reduce
from operator import mul

def all_fixed_length_sublists(arr, width):
    return (sublist for sublist in [arr[i:i+width] for i in range(len(arr) - width)])

def flatten(nested_list):
    return list(itertools.chain(*nested_list))

def product(num_list):
    """
    Returns the product of each element of the list, similar to sum(num_list)
    """
    return reduce(mul, num_list, 1)

def prime_factors(n):
    """
    Returns all the prime factors of a positive integer
    """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(int(n))
            break
    return factors

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

def factors(n):
    """
    Returns all factors, including composite factors
    """
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# Taken from http://stackoverflow.com/questions/18833759/python-prime-number-checker
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def int_to_digits(num):
    """
    Returns a generator of the digits of num
    """
    return (int(i) for i in str(num))

def fibonacci(start_index, end_index=None):
    if not end_index:
        end_index = start_index
        start_index = 0
    return itertools.islice(helpers.fibonacci(), 10)



def fibonacci():
    prev = 0
    cur = 1
    while True:
        yield cur
        cur += prev
        prev = cur - prev

def get_nth_fibonacci(n):
    return next((val for i, val in enumerate(fibonacci()) if i == n - 1))

def get_nth_element_of_generator(generator, n):
    """
    Returns same value as list(generator)[n]
    """
    return next(itertools.islice(generator, n, n + 1))

def get_million_primes():
    with open("helpers/primes.txt") as in_file:
        text = in_file.read()
    return [int(p) for p in re.findall("(\d+)", text)]
