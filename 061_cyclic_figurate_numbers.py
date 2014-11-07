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

def compute_six_cyclic_set():
    polygonals = [{n*(n+1)//2 for n in range(1000)},
                  {n*n for n in range(1000)},
                  {n*(3*n-1)//2 for n in range(1000)},
                  {n*(2*n-1) for n in range(1000)},
                  {n*(5*n-3)//2 for n in range(1000)},
                  {n*(3*n-2) for n in range(1000)}]

    polygonals_together = frozenset(itertools.chain(*polygonals))

    # Maps the first two digits to the last two digits
    cycle_map = collections.defaultdict(set)

    for num in range(1000, 10000):
        if num in polygonals_together:
            cycle_map[str(num)[:2]].add(str(num)[2:])

    # Convert the two-digit string maps to integers
    # Ensure that each of the numbers is four digits
    cyclic_sets = []
    for path in generate_valid_paths(cycle_map):
        cyclic_set = [int(path[i] + path[i+1]) for i in range(len(path) - 1)]
        cyclic_set.append(int(path[-1] + path[0]))

        # Ensure that all elements are 4 digits
        if all(len(str(num)) == 4 for num in cyclic_set):
            cyclic_sets.append(cyclic_set)

    for cyclic_set in cyclic_sets:
        for permutation in itertools.permutations(cyclic_set):
            if all(permutation[i] in polygonals[i] for i in range(6)):
                return cyclic_set

def main():
    cyclic_set = compute_six_cyclic_set()
    answer = sum(cyclic_set)
    print(answer)

if __name__ == '__main__':
    main()