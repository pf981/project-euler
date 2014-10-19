def get_triangle():
    triangle = []
    with open("p067_triangle.txt") as in_file:
        for row in in_file:
            triangle.append([int(word) for word in row.split()])
    return triangle

def main():
    triangle = get_triangle()

    for row in reversed(range(len(triangle) - 1)):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])

    answer = triangle[0][0]
    print(answer)

if __name__ == '__main__':
  main()
