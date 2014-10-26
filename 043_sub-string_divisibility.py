import itertools

def is_sub_string_divisible(digits_str):
    """
    Returns True if the substrings are divisible by primes
    """
    for i, prime in enumerate([2, 3, 5, 7, 11, 13 ,17], start=1):
        if int(digits_str[i:i+3]) % prime != 0:
            return False
    return True

def main():
    # Find the sum of all sub-string divisible 9-digit pandigitals
    answer = sum(int(''.join(s))
                 for s in itertools.permutations('1234567890')
                 if is_sub_string_divisible(''.join(s)))
    print(answer)

if __name__ == '__main__':
    main()
