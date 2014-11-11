# This is a clearer (but less generalised) version based off the c++ code in
# https://projecteuler.net/thread=68;page=8
import collections
import itertools
import operator

def simplify(ring):
    """
    Rotates the ring such that the smallest tuple is first
    """
    index_of_smallest_line = min(enumerate(ring), key=operator.itemgetter(1))[0]

    ring = collections.deque(ring)
    ring.rotate(-index_of_smallest_line)

    return list(ring)

def generate_rings():
    """
    Yields all simplified and unique rings as a list of tuples representing
    the lines of the ring
    """
    for perm in itertools.permutations(list(range(1,10))):
        # A ring consists of 5 lines. Each line has 3 values
        # For the number representation to be 16 digits, 10 must be on the outer edge
        ring = ((10, perm[0], perm[1]),
                (perm[2], perm[1], perm[3]),
                (perm[4], perm[3], perm[5]),
                (perm[6], perm[5], perm[7]),
                (perm[8], perm[7], perm[0]))

        # If all the lines of the ring sum to the same value
        if all(sum(line) == sum(ring[0]) for line in ring):
            yield simplify(ring)

def main():
    answer = max(int(''.join(str(n) for n in itertools.chain(*ring)))
                 for ring in generate_rings())

    print(answer)

if __name__ == '__main__':
    main()