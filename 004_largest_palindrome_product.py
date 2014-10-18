import itertools

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    # Explicitly convert generator to a list as we need to iterate over it twice
    loop_range = list(reversed(range(100, 1000)))
#    for x, y in itertools.product(loop_range, loop_range2):
#        if is_palindrome(x * y):
#            print(x * y)

    print(max(x*y for x, y in itertools.product(loop_range, loop_range) if is_palindrome(x*y)))


if __name__ == '__main__':
  main()
