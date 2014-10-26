# This is a significantly more efficient solution that uses toposort to sort the graph
from toposort import toposort
import collections
import re

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

    sorted_graph = toposort(graph)

    # sorted_graph is a list of single-element sets.
    # This line converts that into a string
    backwards_answer = ''.join([next(iter(item)) for item in sorted_graph])

    # However, due to the way we sorted it, the answer is backwards
    answer = backwards_answer[::-1]

    print(answer)

if __name__ == '__main__':
    main()
