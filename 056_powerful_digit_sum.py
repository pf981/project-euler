# This is just the simplest brute force method, but it still runs in 0.4 seconds
from helpers import helpers

def main():
    answer = max(sum(helpers.int_to_digits(a**b)) for a in range(100) for b in range(100))
    print(answer)


if __name__ == '__main__':
    main()
