import collections
import itertools
import re

def is_possible_password(candidate, graph):
    """
    Returns true if the candidate would satisfy the password requirements
    """
    # For each digit that has known digits that must follow it
    for key in graph:
        index_of_key = candidate.find(key)

        # If the key is not present in the candidate password
        if index_of_key == -1:
            return False

        # For each digit that must follow the key
        for must_follow_key in graph[key]:
            # If that digit cannot be found after the key
            if candidate.find(must_follow_key, index_of_key) == -1:
                return False
    return True

def connections(attempt):
    # digit1 is the key
    for i, digit1 in enumerate(attempt):
        # digit2 is the value. The key must be followed by the value in the password
        for digit2 in attempt[i+1:]:
            yield digit1, digit2


def make_graph(all_attempts):
    """
    Returns a dictionary where the value is a list of the digits that must follow the key
    e.g. attempt "319" means graph['3'] = ['1', '9'] and graph['1'] = ['9']
    """
    graph = collections.defaultdict(set)

    for attempt in all_attempts:
        for before, after in connections(attempt):
            # "after" appears after "before"
            graph[before].add(after)

    return graph

def main():
    with open("p079_keylog.txt") as in_file:
        text = in_file.read()

    all_attempts = re.findall("(\d\d\d)", text)

    # Assume that each of the digits only appears once. If this fails, then the assumption is wrong.
    possible_digits = set(digit for attempt in all_attempts for digit in attempt)

    # graph is a dictionary whose values are the digits that must follow the key
    graph = make_graph(all_attempts)

    # Try all permutations of possible digits
    for permutation in itertools.permutations(possible_digits):
        candidate_password = ''.join(permutation)

        # If this permutation is legitimate
        if (is_possible_password(candidate_password, graph)):
            answer = ''.join(candidate_password)
            break

    print(answer)

if __name__ == '__main__':
    main()
