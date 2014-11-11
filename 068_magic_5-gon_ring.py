# This implementation can solve a generalised n-gon ring. It is very efficient
# as it generates all valid lines and only adds lines to the ring that keep
# the ring valid. However, it is difficult to read. A less efficient and less
# generalised, but more readable solution can be found in
# 068_magic_5-gon_ring2.py
import collections
import itertools
import operator

# "Magic" 5-gon ring
GONS = 5

# The ring contains values 1 to MAX_VALUE
MAX_VALUE = GONS * 2

def generate_all_triples(list_sum):
    """
    Generates tuples of length three such that their values are 1 to MAX_VALUE
    and their sum is list_sum
    """
    for first in range(1, MAX_VALUE+1):
        for second in set(range(1, MAX_VALUE+1)) - set([first]):
            for third in set(range(1, MAX_VALUE+1)) - set([first, second]):
                if first + second + third == list_sum:
                    yield (first, second, third)

def is_valid_line(line, used_lines):
    """
    Returns true if line can be added to used_lines and still produce a valid
    partial ring. False otherwise
    """
    # Warning: Dragons ahead

    # If it is the first line, then it must be valid
    if not used_lines:
        return True

    used_values_list = list(itertools.chain(*used_lines))

    # Ensure that the outer-most value is unique
    if line[0] in used_values_list:
        return False

    # Ensure the middle value of this line is the last value of the
    # previous line, and does not occor elsewhere
    if line[1] != used_lines[-1][2]:
        return False
    elif used_values_list.count(line[1]) > 1:
        return False

    # Ensure the last value of this line is second value of a particular line,
    # and does not occur elsewhere
    if len(used_lines) >= GONS-1:
        if line[2] != used_lines[-GONS+1][1]:
            return False
        elif used_values_list.count(line[2]) > 1:
            return False
    elif used_values_list.count(line[2]) > 0:
        return False

    # Ensure the last value is not in any previous lines (except the first line)
    if any(line[2] in used_lines[i] for i in range(1, min(GONS-2, len(used_lines)))):
        return False

    return True

def generate_lines(used_lines, triples, num_lines):
    """
    Yields all possible rings as a list of triples where each triple represents a line
    """
    if num_lines == 0:
        yield used_lines

    for line in triples:
        # Check if this line will be valid if added
        if not is_valid_line(line, used_lines):
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
    """
    Yields all simplified and unique rings as a list of tuples representing
    the lines of the ring
    """
    rings = set()
    for line_sum in range(30):
        # Generate all triples that add to 9
        triples = list(generate_all_triples(line_sum))

        rings |= set(simplify(ring) for ring in generate_lines([], triples, GONS))
    return rings

def main():
    answer = 0

    # Find the largest 16-digit ring
    for ring in generate_rings():
        for n in itertools.chain(*ring):
            # Convert the list of tuples into an int
            chain_int = int(''.join(str(n) for n in itertools.chain(*ring)))

            # We are looking for a sixteen digit number
            if len(str(chain_int)) == 16:
                answer = max(answer, chain_int)

    print(answer)

if __name__ == '__main__':
    main()
