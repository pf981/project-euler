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

def generate_rings():
    # Generate all triples that add to 9
    triples = list(generate_all_triples())

    # print([*triples[0]], [*triples[1]])
    # print(list(triples[0]) + list(triples[1]))

    # For each set of three lines
    for first in triples:
        for second in triples:
            for third in triples:
                # If the set forms a valid ring
                if first[0] not in list(second) + list(third) and \
                   second[0] not in list(first) + list(third) and \
                   third[0] not in list(first) + list(second):
                    print(first, second, third)



def main():
    generate_rings()
    # answer = max(int(''.join(ring)) for ring in generate_rings())
    # print(answer)

if __name__ == '__main__':
    main()