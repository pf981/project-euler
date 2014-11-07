import itertools
import collections
#import copy

# How many cyclic numbers we are trying to find
TARGET_NUMBERS = 3

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


    cyclic_sets = [(int(a + b), int(b + c), int(c + d))
                  for a, b, c in generate_valid_paths(cycle_map)
                  for d in cycle_map[c]]

    # print(cyclic_sets)
    for cyclic_set in cyclic_sets:
        for permutation in itertools.permutations(cyclic_set):
            # if cyclic_set == (8128, 2882, 8281):
            #     print("!!")
            #     print(permutation[0], permutation[0] in triangles)
            #     print(permutation[1], permutation[1] in squares)
            #     print(permutation[2], permutation[2] in pentagons)
            if permutation[0] in triangles and \
               permutation[1] in squares and \
               permutation[2] in pentagons:
                print(cyclic_set)


    # print(cycle_map)
        # # If the second last digit is zero, then at least one of the cycles will not be
        # # four digits
        # if str(num)[-2]:
        #     continue
        # print(num)

if __name__ == '__main__':
    main()