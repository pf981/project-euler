import re

def score_name(name, index):
    return index * sum(ord(c) - ord('A') + 1 for c in name)


def main():
    with open("p022_names.txt") as in_file:
        text = in_file.read()

    names = sorted(re.findall('"(\w+)"', text))
    # print(score_name("COLIN", names.index("COLIN")))

    answer = sum(score_name(name, i + 1) for i, name in enumerate(names))
    print(answer)


if __name__ == '__main__':
    main()
