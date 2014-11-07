def num_fitting_rectangles(width, height):
    count = 0
    # For each size rectangle
    for w in range(1, width + 1):
        for h in range(1, height + 1):
            # For each position
            for x in range(width - w + 1):
                for y in range(height - h + 1):
                    print(x, y, w, h)
                    count += 1
    return count

def c1(width, height):
    count = 0
    # For each size rectangle
    for w in range(1, width + 1):
        for x in range(width - w + 1):
            count += 1
    print("*", width*(width + 1)/2)
    return count

# It is clear that there probably exist a formula for the count, by looking at it's algorithm... Don't know what it is yet, though
def num_fitting_rectangles2(width, height):
    return width*(width+1)/2*height*(height+1)/2

def main():
    # print(c1(3, 2))
    # return
    print(num_fitting_rectangles(3, 2))
    print(num_fitting_rectangles2(3, 2))


if __name__ == '__main__':
    main()