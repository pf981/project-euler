import collections
import math

MAX_P = 1000

def generate_triples(max_side):
    for a in range(1, max_side):
        for b in range(a, max_side):
            c = int(math.sqrt(a*a + b*b))
            if a*a + b*b == c*c:
                yield [a, b, c]

# def generate_triples_with_sum_under(max_sum):
#     for a in range(1, max_sum):
#         for b in range(a, max_sum):
#             c = int(math.sqrt(a*a + b*b))
#             if a*a + b*b == c*c:
#                 yield [a, b, c]

def main():
    all_p = collections.defaultdict(int)

    # all_p[0] = 99
    # all_p[2] = 100
    # all_p[5] = 4
    # print(max(all_p.keys(), key=lambda key: all_p[key]))

    for a, b, c in generate_triples(MAX_P):
        sides = [a, b, c]
        p = sum(sides)

        if p > MAX_P:
            continue

        all_p[p] += 1
#        print(p, sides)

    answer = max(all_p.keys(), key=lambda key: all_p[key])
    print(answer)




# def main():
#     all_p = collections.defaultdict(int)
#     all_p2 = collections.defaultdict(list)

#     for a in range(1, MAX_P + 1):
#         for b in range(a, MAX_P + 1 - a):
#             # Note: Sqrt is expensive!
#             sides = [a, b, sqrt(a*a + b*b)]
# #                sides = [a, b, c]
#                 all_p2[sum([a, b, c])].append([a, b, c])
#                 all_p[sum([a, b, c])] += 1
# #                print(all_p)
# #                print(sum([a, b, c]), [a, b, c])

#     answer = max(all_p2)
#     print(all_p2)

#     print(answer)

if __name__ == '__main__':
  main()
