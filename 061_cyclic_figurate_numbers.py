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
    triangles = {n*(n+1)//2 for n in range(100)}
    squares = {n*n for n in range(100)}
    pentagons = {n*(3*n-1)//2 for n in range(100)}
    hexagons = {n*(2*n-1) for n in range(100)}
    heptagons = {n*(5*n-3)//2 for n in range(100)}
    octagons = {n*(3*n-2) for n in range(100)}
    polygonals = triangles | squares | pentagons | hexagons | heptagons | octagons

    # Maps the first two digits to the last two digits
    cycle_map = collections.defaultdict(set)

    for num in range(1000, 10000):
        if num in polygonals:
            cycle_map[str(num)[:2]].add(str(num)[2:])


    cyclic_set = [(int(a + b), int(b + c), int(c + d))
                  for a, b, c in generate_valid_paths(cycle_map)
                  for d in cycle_map[c]]

    print(cyclic_set)
    # for path in generate_valid_paths(cycle_map):
    #     for pemutation in itertools.permutations(path):
    #         if


    # print(cycle_map)
        # # If the second last digit is zero, then at least one of the cycles will not be
        # # four digits
        # if str(num)[-2]:
        #     continue
        # print(num)

if __name__ == '__main__':
    main()