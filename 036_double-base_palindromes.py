MAX_RANGE = 1000000

def is_palindrome(n):
    string = str(n)
    return string == string[::-1]

def is_double_palindrome(n):
    return is_palindrome(n) and is_palindrome(str(bin(n))[2:])

def main():
    double_palindromes = [n for n in range(MAX_RANGE) if is_double_palindrome(n)]

    answer = sum(double_palindromes)
    print(answer)

if __name__ == '__main__':
    main()
