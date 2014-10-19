RANGE_MAX = 1000

def main():
    series = sum(n**n for n in range(1, RANGE_MAX + 1))
    answer = str(series)[-10:]
    print(answer)


if __name__ == '__main__':
    main()
