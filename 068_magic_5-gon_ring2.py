# This is a clearer (but less generalised) version based off the c++ code in
# https://projecteuler.net/thread=68;page=8
import itertools
import numpy as np

def generate_rings():
    """
    Yields all simplified and unique rings as a list of tuples representing
    the lines of the ring
    """
    # permutation = range(1, 11)
    for _ in range(3):
        # ring = [[0]*3 for _ in range(3)]
        ring = np.zeros((3, 3), dtype=np.int32)
        yield ring

def main():
    answer = max(int(''.join(str(n) for n in itertools.chain(*ring)))
                 for ring in generate_rings())

    print(answer)

if __name__ == '__main__':
    main()