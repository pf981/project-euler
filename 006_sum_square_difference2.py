# This method is significantly more efficient that version 1
# It is O(1) rather than O(n)
MAX = 100

def main():
    square_of_sum = pow(MAX * (MAX + 1) / 2, 2)
    sum_of_squares = (2 * MAX + 1) * (MAX + 1) * MAX / 6
    answer = int(square_of_sum - sum_of_squares)
    print(answer)


if __name__ == '__main__':
  main()
