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

def main():
    print(num_fitting_rectangles(3, 2))

if __name__ == '__main__':
    main()