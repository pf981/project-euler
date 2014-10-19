from helpers import helpers
from itertools import permutations

MAX_PRIME = 1000000
PRIMES = [p for p in helpers.get_million_primes()[:MAX_PRIME] if p < MAX_PRIME]

def rotations(n):
    string = str(n)
    for i in range(len(string)):
        yield int(string[i:] + string[:i])
        # or: string.append(string.pop(0))

def is_circular(prime):
    # or: return all(rotation in PRIMES for rotation in rotations(prime)))
    for rotation in rotations(prime):
        if not rotation in PRIMES:
            return False
    return True

def main():
    circular_primes = [prime for prime in PRIMES if is_circular(prime)]
    answer = len(circular_primes)
    print(answer)

if __name__ == '__main__':
    main()
