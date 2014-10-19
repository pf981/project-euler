from helpers import helpers
from itertools import permutations

MAX_PRIME = 1000000
PRIMES = [p for p in helpers.get_million_primes()[:MAX_PRIME] if p < MAX_PRIME]

def rotations(n):
    string = str(n)
    for i in range(len(string)):
        yield int(string[i:] + string[:i])

def is_circular(prime):
#    return all(int(rotation) in PRIMES for rotation in permutations(str(prime)))
#    return all(int("".join(rotation)) in PRIMES for rotation in permutations(str(prime)))
#    print([int("".join(rotation)) in PRIMES for rotation in permutations(str(prime))])
#    rotations = [int("".join(rotation)) for rotation in permutations(str(prime))]
#    print(rotations)

    # FIXME: ROTATE not PERMUTE
    # for rotation in permutations(str(prime)):
    #     rotation = "".join(rotation)
    #     print(rotation)
    #     if len(rotation) != len(str(prime)):
    #         return False
    #     if not int(rotation) in PRIMES:
    #         return False
    # return True

#        print(int("".join(rotation)))

    for rotation in rotations(prime):
#        print(rotation)
        if not rotation in PRIMES:
            return False
    return True



def main():
#    print(list(rotations(197)))
    circular_primes = [prime for prime in PRIMES if is_circular(prime)]
#    print(circular_primes)
    answer = len(circular_primes)
    print(answer)

if __name__ == '__main__':
    main()
