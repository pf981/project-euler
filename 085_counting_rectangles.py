MAX_LENGTH = 1000

# # This is the first algorithm I created to compute the number of fitting
# # rectangles. It constructed rectangles of every size that would fit, and
# # determined which positions would be valid. However, examining the
# # algorithm, I could see that it could probably be simplified into a single
# # expression as it is just counting the number of times a loop executes.
# def num_fitting_rectangles(width, height):
#     count = 0
#     # For each size rectangle
#     for w in range(1, width + 1):
#         for h in range(1, height + 1):
#             # For each position
#             for x in range(width - w + 1):
#                 for y in range(height - h + 1):
#                     print(x, y, w, h)
#                     count += 1
#     return count

# This is the optimised version. We note that the following executes N*(N+1)/2 times
#     for w in range(N):
#         for x in range(N - w + 1):
#
# Applying this knowledge to our original algorithm yields
#     num_rectangles = width * (width+1)/2 * height * (height+1)/2
def num_fitting_rectangles(dimensions):
    """
    Returns an integer which represents the number of rectangles that could
    fit in a grid of the given dimensions. dimensions is a tuple containing
    width and height
    """
    width = dimensions[0]
    height = dimensions[1]
    return width * (width+1)/2 * height * (height+1)/2

def main():
    optimal_dimensions = min(((width, height)
                              for width in range(MAX_LENGTH)
                              for height in range(MAX_LENGTH)),
                             key=lambda x: abs(num_fitting_rectangles(x) - 2000000))

    print(optimal_dimensions[0] * optimal_dimensions[1])

if __name__ == '__main__':
    main()