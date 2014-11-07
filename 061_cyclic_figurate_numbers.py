#import itertools
import collections

# How many cyclic numbers we are trying to find
TARGET_NUMBERS = 3

def generate_valid_paths(tree):
    """
    This generates paths from a depth-first tree traversal such that the path
    is TARGET_PAIRS long and every element is adjacent to every other element
    """
    for node, _ in tree.items():
        # nodes_to_visit is a list of tuples. The first element of the tuple
        # is the node to visit. The second is a list representing the path
        # taken to get to that node.
        nodes_to_visit = [(node, set())]

        while nodes_to_visit:
            cur_node = nodes_to_visit.pop()
            cur_path = cur_node[1] | {cur_node[0]}

            for child in tree[cur_node[0]]:
                # If the child hasn't been visited and the child contains
                # every element in the path
                if child not in cur_path:
                    # Prepend the node and the path
                    nodes_to_visit.insert(0, (child, cur_path))

            if len(cur_path) == TARGET_NUMBERS:
                yield cur_path
# FIXME: USE LIST

def main():
    # Maybe map every two digit number to pentagonal numbers that start with those digits
    # generate_cycle(8128)

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

    for path in generate_valid_paths(cycle_map):
        print(path)

    # print(cycle_map)
        # # If the second last digit is zero, then at least one of the cycles will not be
        # # four digits
        # if str(num)[-2]:
        #     continue
        # print(num)

if __name__ == '__main__':
    main()