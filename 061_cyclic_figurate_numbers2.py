# This version is identical to the previous version, but uses recursion rather
# that iteration using a stack. It has poorer performance, but this was more
# an exercise (recursing with generators) than an attempt to increase
# performance. It should be noted that python does not support tail recursion
# optimisation and only supports 1000 levels of recursion, so this
# implementation will fail if it is expanded.
import itertools
import collections
#import copy

# How many cyclic numbers we are trying to find
TARGET_NUMBERS = 6

def traverse_path(node, path, tree):
    if len(path) == 6:
        yield path
        return

    for child in tree[node]:
        for complete_path in traverse_path(child, path + [node], tree):
            yield complete_path

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
        for path in traverse_path(node, [], tree):
            yield path

def compute_six_cyclic_set():
    """
    Returns a 6 element list representing that is the cyclic set where each
    element is polygonal
    """
    # polygonals[0] is the set of all triangulars etc.
    # In order: triangulars, squares, pentagonals, hexagonals, heptagonals,
    # octagonals
    polygonals = [{n*(n+1)//2 for n in range(1000)},
                  {n*n for n in range(1000)},
                  {n*(3*n-1)//2 for n in range(1000)},
                  {n*(2*n-1) for n in range(1000)},
                  {n*(5*n-3)//2 for n in range(1000)},
                  {n*(3*n-2) for n in range(1000)}]

    # Merge them into a single set, so it is easier to determine if a number
    # is in any of them
    polygonals_together = frozenset(itertools.chain(*polygonals))

    # For each of the four-digit polygonal numbers, map the first two digits
    # to the last two digits
    cycle_map = collections.defaultdict(set)
    for num in range(1000, 10000):
        if num in polygonals_together:
            cycle_map[str(num)[:2]].add(str(num)[2:])

    # Generate every six-long set of cyclic polygonals and convert the
    # two-digit string maps to integers. Ie cycle_map['81'] == '28' -> 8128
    # Ensure that each of the numbers is four digits
    cyclic_sets = []
    for path in generate_valid_paths(cycle_map):
        cyclic_set = [int(path[i] + path[i+1]) for i in range(len(path) - 1)]
        cyclic_set.append(int(path[-1] + path[0]))

        # Ensure that all elements are 4 digits
        if all(len(str(num)) == 4 for num in cyclic_set):
            cyclic_sets.append(cyclic_set)

    # Find which of the candidate sets contains all different
    # polygonals. E.g. not all triangular numbers
    for cyclic_set in cyclic_sets:
        # To do this, just permute the set and check if the first is
        # triangular, the second is square etc
        for permutation in itertools.permutations(cyclic_set):
            if all(permutation[i] in polygonals[i] for i in range(6)):
                return cyclic_set

def main():
    cyclic_set = compute_six_cyclic_set()
    answer = sum(cyclic_set)
    print(answer)

if __name__ == '__main__':
    main()