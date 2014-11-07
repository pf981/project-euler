MAX_LENGTH = 1000

def num_fitting_rectangles2(width, height):
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

# It is clear that there probably exist a formula for the count, by looking at it's algorithm... Don't know what it is yet, though
def num_fitting_rectangles(dimensions):
    width = dimensions[0]
    height = dimensions[1]
    return width * (width+1)/2 * height * (height+1)/2

def main():
    optimal_dimensions = min(((width, height)
                              for width in range(MAX_LENGTH)
                              for height in range(MAX_LENGTH)),
                             key=lambda x: abs(num_fitting_rectangles(x) - 2000000))
    # optimal_dimensions = min(((width, height)
    #                           for width in range(MAX_LENGTH)
    #                           for height in range(MAX_LENGTH)),
    #                          key=lambda x: abs(num_fitting_rectangles(x[0], x[1]) - 2000000))

    print(optimal_dimensions, num_fitting_rectangles(optimal_dimensions))
    print(optimal_dimensions[0] * optimal_dimensions[1])
    # 2000000 = width * (width+1)/2 * height * (height+1)/2
    # print(c1(3, 2))
    # return
    # print(num_fitting_rectangles(3, 2))
    # print(num_fitting_rectangles2(3, 2))


if __name__ == '__main__':
    main()