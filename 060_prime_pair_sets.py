import collections
import copy
import sympy
from sympy.ntheory.primetest import isprime

MAX_PRIMES = 20
TARGET_PAIRS = 4

def find_valid_path(tree):
    for node, _ in tree.items():
        # nodes_to_visit is a list of tuples. The first element of the tuple
        # is the node to visit. The second is a list representing the path
        # taken to get to that node.
        nodes_to_visit = [(node, set())]

        # print(node)
        while nodes_to_visit:
            cur_node = nodes_to_visit.pop()
            print("@", cur_node)
            for child in tree[cur_node[0]]:
                # Prepend the node and the path
                print(child, cur_node[1], cur_node[0])
                print(nodes_to_visit)
                nodes_to_visit.insert(0, (child, cur_node[1] | {cur_node[0]}))
                # nodes_to_visit.insert(0, (child, set(cur_node[1])))
                # nodes_to_visit.insert(0, (child, cur_node[1].union(set(cur_node[0]))))
                # nodes_to_visit.insert(0, (child, cur_node[1] | set(cur_node[0])))
            # nodes_to_visit = tree[cur_node] + nodes_to_visit


            print(cur_node, nodes_to_visit)
        break


# def find_valid_path(tree):
#     for node, _ in tree.items():
#         nodes_to_visit = [node]
#         cur_path = [node]

#         # print(node)
#         while nodes_to_visit:
#             cur_node = nodes_to_visit.pop()
#             nodes_to_visit = tree[cur_node] + nodes_to_visit
#             print(cur_node, nodes_to_visit)

def concat_ints(a, b):
    return int(str(a) + str(b))

def is_cat_pair(pair):
    return isprime(concat_ints(pair[0], pair[1]))

def main():
    find_valid_path({1: set([2]), 2: set([3, 4]), 3: set(), 4: set()})
    return
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
    # paired_with = collections.defaultdict(list)
    # for p1, p2 in all_pairs:
    #     if is_cat_pair((p1, p2)):
    #         paired_with[p1].append(p2)

    # print(paired_with)

    # Want:
    # 3  : 7 109 673
    # 7  : 3 109 673
    # 109: 3 7   673
    # 673: 3 7   109

    # THIS IS A TREE!!! - then maybe the pairs should be both concatenate so the tree is unidirectional
    #        3
    #   7   109    67

    find_valid_path(paired_with)
    # for a in primes:
    #     final_primes = copy.copy(paired_with[a])
    #     for b in paired_with[a]:
    #         if b not in final_primes:
    #             continue
    #         final_primes &= paired_with[b]
    #     print(final_primes)


    # FIXME: Could trim the set by only considering primes who have 5 or more paired primes
    # for starter in primes:
    #     final_primes = copy.copy(paired_with[starter])
    #     for other in paired_with[starter]:
    #         if other not in final_primes:
    #             continue
    #         final_primes &= paired_with[other]
    #     print(final_primes)

        # final_primes = [starter] + paired_with[starter]
        # for other in final_primes:

        # print(starter, final_primes)

    print(primes)
    # print(pairs)

    pass

if __name__ == '__main__':
    main()