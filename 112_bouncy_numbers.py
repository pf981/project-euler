import itertools

TARGET_PROPORTION = 0.5

def is_bouncy(n):
    list_n = list(str(n))
    left_bouncy = sorted(list_n)
    right_bouncy = list(reversed(left_bouncy))

    return list_n == left_bouncy or list_n == right_bouncy

def main():
    num_bouncy = 0

    for n in itertools.count(1):
        if is_bouncy(n):
            num_bouncy += 1
        if num_bouncy / n > TARGET_PROPORTION:
            answer = n
            break

    print(answer)

if __name__ == '__main__':
    main()