import itertools
import collections
#import copy

# How many cyclic numbers we are trying to find
TARGET_NUMBERS = 6

def generate_valid_paths(tree):
    """
    This generates paths from a depth-first tree traversal such that the path
    is TARGET_NUMBERS long
    """
    # We use list(keys) here to get a deep copy. An error occured when using copy.copy(keys)
    for node in list(tree.keys()):
        # nodes_to_visit is a list of tuples. The first element of the tuple
        # is the node to visit. The second is a list representing the path
        # taken to get to that node.
        nodes_to_visit = [(node, [])]

        while nodes_to_visit:
            cur_node = nodes_to_visit.pop()
            cur_path = cur_node[1] + [cur_node[0]]

            # If the path is longer than we need
            if len(cur_path) > TARGET_NUMBERS:
                # Don't bother
                continue

            for child in tree[cur_node[0]]:
                # Prepend the node and the path
                nodes_to_visit.insert(0, (child, cur_path))

            if len(cur_path) == TARGET_NUMBERS:
                yield cur_path

def main():
    triangles = {n*(n+1)//2 for n in range(1000)}
    squares = {n*n for n in range(1000)}
    pentagons = {n*(3*n-1)//2 for n in range(1000)}
    hexagons = {n*(2*n-1) for n in range(1000)}
    heptagons = {n*(5*n-3)//2 for n in range(1000)}
    octagons = {n*(3*n-2) for n in range(1000)}
    polygonals = triangles | squares | pentagons | hexagons | heptagons | octagons

    # print(triangles)
    # print(8128 in triangles)
    # return

    # Maps the first two digits to the last two digits
    cycle_map = collections.defaultdict(set)

    for num in range(1000, 10000):
        if num in polygonals:
            cycle_map[str(num)[:2]].add(str(num)[2:])


    # Convert the two-digit string maps to integers
    # Ensure that each of the numbers is four digits
    cyclic_sets = [(int(a + b), int(b + c), int(c + d), int(d + e), int(e + f), int(f + a))
                  for a, b, c, d, e, f in generate_valid_paths(cycle_map)
                  if len(str(int(a + b))) == len(str(int(b + c))) == len(str(int(c + a))) == 4]
    # cyclic_sets = [(int(a + b), int(b + c), int(c + a))
    #               for a, b, c in generate_valid_paths(cycle_map)
    #               if len(str(int(a + b))) == len(str(int(b + c))) == len(str(int(c + a))) == 4]

    for cyclic_set in cyclic_sets:
        for permutation in itertools.permutations(cyclic_set):
            if permutation[0] in triangles and \
               permutation[1] in squares and \
               permutation[2] in pentagons and \
               permutation[3] in hexagons and \
               permutation[4] in heptagons and \
               permutation[5] in octagons:
                print(cyclic_set, sum(cyclic_set))

if __name__ == '__main__':
    main()