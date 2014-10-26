import itertools

def generate_pentagonal(num_to_generate):
    for n in range(1, num_to_generate):
        yield n * (3*n - 1) // 2

def get_min_distance():
    pentagonals = frozenset(generate_pentagonal(10000))

    # print(1560090 in pentagonals)

    # for distance in itertools.count(1):
    for distance in range(5482600, 10000000):
    # for distance in range(4000000, 10000000):
        # print(distance)
        for pentagonal in pentagonals:
            pentagonal2 = pentagonal - distance
            # if pentagonal == 1560090:
            #     print(pentagonal, pentagonal2, distance)
            if (pentagonal2 in pentagonals
              and pentagonal + pentagonal2 in pentagonals
              and pentagonal - pentagonal2 in pentagonals):
                print(pentagonal, pentagonal2)
                return distance

# def get_min_distance():
#     pentagonals = list(generate_pentagonal(10000))
#     set_pentagonals = frozenset(pentagonals)

#     # For each pair of pentagonal numbers
#     for i, pentagonal1 in enumerate(pentagonals):
#         for pentagonal2 in pentagonals[i+1:]:
#             # If their sum and difference are pentagonal
#             if (pentagonal2 + pentagonal1 in set_pentagonals
#               and pentagonal2 - pentagonal1 in set_pentagonals):
#                 # Presume that the distance is minimised (if it isn't, try a different approach)
#                 print(pentagonal1, pentagonal2)
#                 return pentagonal2 - pentagonal1

def main():
    answer = get_min_distance()
    print(answer)


if __name__ == '__main__':
    main()
