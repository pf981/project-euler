import itertools

# "Magic" 3-gon ring
GONS = 3

# The ring contains values 1 to MAX_VALUE
MAX_VALUE = GONS * 3

def generate_all_triples():
    for first in range(1, MAX_VALUE+1):
        for second in range(1, MAX_VALUE+1):
            for third in range(1, MAX_VALUE+1):
                if first + second + third == 9:
                    yield (first, second, third)

# def candidate_ring(triples, num_lines):
#     # if num_lines == 0:
#     #     yield []
#     if num_lines == 1:
#         for triple in triples:
#             yield [triple]

#     for triple in triples:
#         for others in candidate_ring(triples, num_lines-1):
#             yield [triple] + others

def candidate_ring(used_lines, triples, num_lines):
    if num_lines == 0:
        yield used_lines

    for line in triples:
        # Check if this line will be valid if added
        if line[0] in list(itertools.chain(*used_lines)):
            continue

        for ring in candidate_ring(used_lines + [line], triples, num_lines-1):
            yield ring
        # yield candidate_ring(used_lines + [line], triples, num_lines-1)
        # for others in candidate_ring(used_lines + [triple], triples, num_lines-1):
        #     yield [line] + others

def generate_rings():
    # Generate all triples that add to 9
    triples = list(generate_all_triples())

    for ring in candidate_ring([], triples, GONS):
        print("@", ring)

    # # For each set of three lines
    # for first in triples:
    #     for second in triples:
    #         for third in triples:
    #             # If the set forms a valid ring
    #             # if first[0] not in list(second) + list(third) and \
    #             #    second[0] not in list(first) + list(third) and \
    #             #    third[0] not in list(first) + list(second):
    #             #     print(first, second, third)
    #             print(first, second, third)



def main():
    generate_rings()
    # answer = max(int(''.join(ring)) for ring in generate_rings())
    # print(answer)

if __name__ == '__main__':
    main()