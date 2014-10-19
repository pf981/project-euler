# BASE_RANGE = range(2, 6)
# EXPONENT_RANGE = range(2, 6)
BASE_RANGE = range(2, 101)
EXPONENT_RANGE = range(2, 101)

def main():
    sequence = set([a**b for a in BASE_RANGE for b in EXPONENT_RANGE])

    # print(sequence)
    answer = len(sequence)
    print(answer)


if __name__ == '__main__':
    main()
