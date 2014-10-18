def collatz_count(n):
    length = 1
    while n != 1:
        length += 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3 * n + 1

    return length

def main():
    # Find the number with the highest collatz count
    answer = max([n for n in range(1, 1000000)], key=lambda x: collatz_count(x))
    print(answer)

if __name__ == '__main__':
  main()
