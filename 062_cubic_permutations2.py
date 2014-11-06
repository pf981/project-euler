import collections

MAX_CUBES = 50000

def main():
    # cube_counts' key is a sorted cube and its value is the number of cubes
    # that share that sorted form
    cube_counts = collections.defaultdict(int)

    # cubes is used to determine what cubes resulted in a particular sorted
    # form. It maps the sorted form to a list of cubes which share that sorted
    # form
    cubes = collections.defaultdict(list)

    # Generate many cubes
    for n in range(MAX_CUBES):
        cube = n**3
        sorted_cube = ''.join(sorted(str(cube)))
        cube_counts[sorted_cube] += 1
        cubes[sorted_cube].append(cube)

    # The answer is the smallest cube whose count is 5
    answer = min(min(cubes[sorted_cube]) for sorted_cube, count in cube_counts.items() if count == 5)

    print(answer)

if __name__ == '__main__':
    main()
