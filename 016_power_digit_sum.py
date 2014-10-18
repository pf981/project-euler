from helpers import helpers

def main():
    answer = sum(helpers.int_to_digits(2**1000))
    print(answer)

if __name__ == '__main__':
  main()
