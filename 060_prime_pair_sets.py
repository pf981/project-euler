import collections
import sympy
from sympy.ntheory.primetest import isprime

MAX_PRIMES = 1000
TARGET_PAIRS = 4

def generate_valid_paths(tree):
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
                if child not in cur_path and tree[child] >= cur_path:
                    # Prepend the node and the path
                    nodes_to_visit.insert(0, (child, cur_path))

            if len(cur_path) == TARGET_PAIRS:
                yield cur_path

def concat_ints(a, b):
    return int(str(a) + str(b))

def is_cat_pair(pair):
    return isprime(concat_ints(pair[0], pair[1]))

def main():
    primes = list(sympy.sieve.primerange(2, MAX_PRIMES))

    all_pairs = [(p1, p2)
             for p1 in primes
             for p2 in primes]

    # paired_with maps a prime to a list of primes. This means that all the
    # elements in the value can be appended to the key to form a prime
    # paired_with[2] = [3, 11, 23] means that 23, 211 and 223 are all primes
    paired_with = collections.defaultdict(set)
    for p1, p2 in all_pairs:
        if is_cat_pair((p1, p2)):
            paired_with[p1].add(p2)

    answer = min(generate_valid_paths(paired_with), key=lambda x: sum(x))
    print(answer)

if __name__ == '__main__':
    main()