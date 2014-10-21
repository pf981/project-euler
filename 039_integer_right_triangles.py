import collections
import math

MAX_P = 1000

def generate_triples(max_side):
    """
    Yields all unique pythagorean whose sides are less than max_side
    """
    for a in range(1, max_side):
        for b in range(a, max_side):
            c_double = math.sqrt(a*a + b*b)
            c = int(c_double)
            if c == c_double:
                yield [a, b, c]

def main():
    all_p = collections.defaultdict(int)

    for a, b, c in generate_triples(MAX_P):
        sides = [a, b, c]
        p = sum(sides)

        if p > MAX_P:
            continue

        all_p[p] += 1

    answer = max(all_p.keys(), key=lambda key: all_p[key]) # Find the key with the max value of a dict
    print(answer)

if __name__ == '__main__':
  main()
