NUMS_TO_GENERATE = 1000000

def main():
    # Generate triangular numbers
    triangular_nums = frozenset((n * (n+1) // 2 for n in range(286, NUMS_TO_GENERATE)))

    # Generate pentagonal numbers
    pentagonal_nums = frozenset((n * (3*n-1) // 2 for n in range(166, NUMS_TO_GENERATE)))

    # Generate hexagonal numbers
    hexagonal_nums = frozenset((n * (2*n-1) for n in range(144, NUMS_TO_GENERATE)))

    for num in triangular_nums:
        if num in pentagonal_nums and num in hexagonal_nums:
            answer = num
            break

    print(answer)

if __name__ == '__main__':
  main()
