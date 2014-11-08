def read_triangles():
    triangles = []
    for line in open("p102_triangles.txt"):
        splits = [int(s) for s in line.split(',')]

        # Split the line into three two-wide tuples representing the three
        # coordinates
        coords = tuple(tuple(splits[i:i+2]) for i in range(0, len(splits), 2))
        triangles.append((coords))

    return triangles

def determinant(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def contains_origin(triangle):
    origin = (0, 0)
    det1 = determinant(origin, triangle[0], triangle[1]) < 0
    det2 = determinant(origin, triangle[1], triangle[2]) < 0
    det3 = determinant(origin, triangle[2], triangle[0]) < 0
    return det1 == det2 == det3

def main():
    triangles = read_triangles()
    answer = sum(1 for triangle in triangles if contains_origin(triangle))
    print(answer)

if __name__ == '__main__':
    main()