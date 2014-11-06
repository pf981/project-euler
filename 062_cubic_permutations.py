# This will probably work, but it takes too long to compute. This method gets
# all permutations of each cube and determines if they are cubes too. A better
# way is to generate all cubes in a range and count them. This better solution
# is implemented in 062_cubic_permutations.py
import itertools

def is_cube(n):
    return round(n**(1/3.0))**3 == n

def generate_permutations(n):
    for permutation in set(itertools.permutations(str(n))):
        permutation_value = int(''.join(permutation))

        # If it has leading zeros, ignore it
        if len(str(permutation_value)) != len(str(n)):
            continue

        yield permutation_value


def main():
    for n in itertools.count(1):
        cube = n**3

        # For each permutation of that cube
        cubes = [permutation for permutation in generate_permutations(cube) if is_cube(permutation)]
        counts = len(cubes)

        # If five of those permutations were cubes
        if counts == 5:
            answer = min(cubes)
            break

    print(answer)

if __name__ == '__main__':
    main()
