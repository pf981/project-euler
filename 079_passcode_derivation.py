import collections
import re

def connections(attempt):
    for i, digit1 in enumerate(attempt):
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

    graph = make_graph(all_attempts)
    print(graph)

    # possible_numbers = set(digit for digit in attempt for attempt in all_attempts)
    # possible_numbers = set(digit for attempt in all_attempts for digit in attempt)
    # print(possible_numbers)
    # passcode_guess = ''

    # # for number in (triple for triple in numbers):
    # for triple in numbers:
    #     index = 0
    #     for digit in triple:
    #         print(digit)

    #         index = passcode_guess.find(digit, index)
    #         if index == -1:
    #             passcode_guess += digit
    #     # print(index)
    #     # break

    # print(passcode_guess)

    # for possible_passcode in itertools.count(1):
    #     if is

    # answer = len(passcode_guess) + 1
    # print(answer)

if __name__ == '__main__':
    main()
