import re

def main():
    # triangles = re.findall(r'(-?\d+),(-?\d+),(-?\d+),(-?\d+),(-?\d+),(-?\d+)', open("p102_triangles.txt").read())
    # print(int('-1'))
    # return
    triangles = []
    for line in open("p102_triangles.txt"):
        splits = [int(s) for s in line.split(',')]
        coords = tuple(tuple(splits[i:i+2]) for i in range(0, len(splits), 2))
        print(coords)
        triangles.append((splits))
        # (split[:2], split[2:])
    # [tuple()
    # coords = open("p102_triangles.txt").read().split(',')
    # print(coords[:5])

if __name__ == '__main__':
    main()