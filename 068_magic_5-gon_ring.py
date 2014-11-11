import collections
import itertools
import operator

# "Magic" 3-gon ring
GONS = 5

# The ring contains values 1 to MAX_VALUE
MAX_VALUE = GONS * 2

def generate_all_triples(list_sum):
    for first in range(1, MAX_VALUE+1):
        for second in set(range(1, MAX_VALUE+1)) - set([first]):
            for third in set(range(1, MAX_VALUE+1)) - set([first, second]):
                if first + second + third == list_sum:
                    yield (first, second, third)

def is_valid_line(line, used_lines):
    # If it is the first line, then it must be valid
    if not used_lines:
        return True

    used_values_list = list(itertools.chain(*used_lines))

    # Ensure that the outer-most value is unique
    if line[0] in used_values_list:
        return False

    # Ensure the middle value of this line is the last value of the
    # previous line
    if line[1] != used_lines[-1][2]:
        return False
    elif used_values_list.count(line[1]) > 1:
        return False

    # FIXME: FIX BELOW, above should be fine
    # Ensure the last value of this line is second value of the line two back
    # if len(used_lines) >= GONS-1 and line[2] != used_lines[-GONS+1][1]:
    #     return False
    if len(used_lines) >= GONS-1:
        if line[2] != used_lines[-GONS+1][1]:
            return False
        elif used_values_list.count(line[2]) > 1:
            return False
    elif used_values_list.count(line[2]) > 0:
        return False


    # Ensure the last value is not in any previous lines # FIXME: Except one of them
    # Count how many times line[2] occurs in used_lines. If the length is big, it should be 1, if the length is small, it should be 0. FIXME: This isn't fixed yet
    if any(line[2] in used_lines[i] for i in range(1, min(GONS-2, len(used_lines)))):
    # if any(line[2] in used_lines[i] for i in range(1, GONS-2)):
    # if line[2] in used_lines[-1]:
        return False

    return True


def generate_lines(used_lines, triples, num_lines):
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
    # answer = max(int(''.join(str(s) for s in ring)) for ring in generate_rings())
    # for ring in generate_rings():
        # print(int(''.join(str(n) for n in itertools.chain(*ring))))
    # answer = max(int(''.join(str(n) for n in itertools.chain(*ring)))
    #              for ring in generate_rings())
    answer = 0
    for ring in generate_rings():
        for n in itertools.chain(*ring):
            chain_int = int(''.join(str(n) for n in itertools.chain(*ring)))
            if len(str(chain_int)) == 16:
                answer = max(answer, chain_int)
    # FIXME: Something is wrong with the validation. There should only be a maximum of two of any value, but this finds one with three tens
    print(answer)

if __name__ == '__main__':
    main()