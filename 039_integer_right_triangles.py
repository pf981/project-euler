import collections

MAX_P = 10

def main():
    all_p = collections.defaultdict(int)
    all_p2 = collections.defaultdict(list)

    for a in range(1, MAX_P + 1):
        for b in range(a, MAX_P + 1 - a):
            for c in range(b, MAX_P + 1 - a - b):
#                sides = [a, b, c]
                all_p2[sum([a, b, c])].append([a, b, c])
                all_p[sum([a, b, c])] += 1
#                print(all_p)
#                print(sum([a, b, c]), [a, b, c])

    answer = max(all_p2)
    print(all_p2)

    print(answer)

if __name__ == '__main__':
  main()
