import itertools

TARGET_PROPORTION = 0.99

def is_bouncy(n):
    """
    Returns true if n's digits are not in ascending or descending order
    False otherwise
    """
    list_n = list(str(n))
    left_to_right = sorted(list_n)
    right_to_left = list(reversed(left_to_right))

    return list_n != left_to_right and list_n != right_to_left

def main():
    num_bouncy = 0

    for n in itertools.count(1):
        if is_bouncy(n):
            num_bouncy += 1

        # Calculate the proportion of bouncy to non-bouncy numbers
        if num_bouncy / n > TARGET_PROPORTION:
            answer = n - 1
            break

    print(answer)

if __name__ == '__main__':
    main()