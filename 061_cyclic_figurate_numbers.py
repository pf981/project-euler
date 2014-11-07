#import itertools
import collections

# def generate_cycle(n):
#     n_deque = collections.deque(str(n))
# #    for _ in len(n):
#     print(n_deque)


def main():
    # Maybe map every two digit number to pentagonal numbers that start with those digits
    # generate_cycle(8128)

    triangles = {n*(n+1)//2 for n in range(100)}
    squares = {n*n for n in range(100)}
    pentagons = {n*(3*n-1)//2 for n in range(100)}
    hexagons = {n*(2*n-1) for n in range(100)}
    heptagons = {n*(5*n-3)//2 for n in range(100)}
    octagons = {n*(3*n-2) for n in range(100)}
    polygonals = triangles | squares | pentagons | hexagons | heptagons | octagons

    # Maps the first two digits to the last two digits
    cycle_map = collections.defaultdict(set)

    for num in range(1000, 10000):
        if num in polygonals:
            cycle_map[str(num)[:2]].add(str(num)[2:])

    print(cycle_map)
        # # If the second last digit is zero, then at least one of the cycles will not be
        # # four digits
        # if str(num)[-2]:
        #     continue
        # print(num)

if __name__ == '__main__':
    main()