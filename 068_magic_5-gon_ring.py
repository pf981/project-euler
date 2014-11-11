import collections
import itertools
import operator

# "Magic" 3-gon ring
GONS = 3

# The ring contains values 1 to MAX_VALUE
MAX_VALUE = GONS * 2

def generate_all_triples(list_sum):
    for first in range(1, MAX_VALUE+1):
        for second in set(range(1, MAX_VALUE+1)) - set([first]):
            for third in set(range(1, MAX_VALUE+1)) - set([first, second]):
                if first + second + third == list_sum:
                    yield (first, second, third)
# def generate_all_triples():
#     for first in range(1, MAX_VALUE+1):
#         for second in set(range(1, MAX_VALUE+1)) - set([first]):
#             for third in set(range(1, MAX_VALUE+1)) - set([first, second]):
#                 if first + second + third == 9:
#                     yield (first, second, third)

# FIXME: Remove duplicates
def generate_lines(used_lines, triples, num_lines):
    if num_lines == 0:
        yield used_lines

    for line in triples:
        # Check if this line will be valid if added
        if used_lines:
            # Ensure that the outer-most value is unique
            if line[0] in list(itertools.chain(*used_lines)):
                continue

            # Ensure the middle value of this line is the last value of the
            # previous line
            if line[1] != used_lines[-1][2]:
                continue

            # Ensure the last value of this line is second value of the line two back
            if len(used_lines) >= 2 and line[2] != used_lines[-2][1]:
                continue

            # Ensure the last value is not in the previous line
            if line[2] in used_lines[-1]:
                continue

        # Recursively add all the next rings
        for ring in generate_lines(used_lines + [line], triples, num_lines-1):
            yield ring

def simplify(ring):
    """
    Rotates the ring such that the smallest tuple is first
    """
    index_of_smallest_tuple = min(enumerate(ring), key=operator.itemgetter(1))[0]

    ring = collections.deque(ring)
    ring.rotate(-index_of_smallest_tuple)

    return tuple(ring)

def generate_rings():
    rings = set()
    for line_sum in range(30):
        # Generate all triples that add to 9
        triples = list(generate_all_triples(line_sum))

        rings |= set(simplify(ring) for ring in generate_lines([], triples, GONS))
    return rings

def main():
    for ring in generate_rings():
        for line in ring:
            print("{0},{1},{2};".format(*line), end="")
        print()

        # print(list(itertools.chain(*ring)))
    # answer = max(int(''.join(ring)) for ring in generate_rings())
    # print(answer)

if __name__ == '__main__':
    main()