RANGE_MAX = 101

def main():
    sum_of_squares = sum((x*x for x in range(RANGE_MAX)))
    square_of_sum = pow(sum((x for x in range(RANGE_MAX))), 2)
    answer = square_of_sum - sum_of_squares
    print(answer)


if __name__ == '__main__':
  main()
