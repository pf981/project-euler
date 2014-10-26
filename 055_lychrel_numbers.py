from helpers import helpers

def is_lychrel(n):
    palindrom_candidate = n

    # Attempt the process 50 times
    for _ in range(50):
        # Add the reverse of the number
        palindrom_candidate += int(str(palindrom_candidate)[::-1])

        # If we are left with a palindrome
        if helpers.is_palindrome(palindrom_candidate):
            # It must not be a lychrel number
            return False

    # If it didn't find a palindrome within 50 iterations, assume it is a
    # lychrel number
    return True

def main():
    lychrel_numbers = [n
                       for n in range(10000)
                       if is_lychrel(n)]

    answer = len(lychrel_numbers)
    print(answer)


if __name__ == '__main__':
    main()
