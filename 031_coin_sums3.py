# This is a much better solution, based of the pdf from Project Euler
DESIRED_TOTAL = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def main():
    ways = [0] * (DESIRED_TOTAL + 1)
    ways[0] = 1

    for coin in COINS:
        for coin_index in range(coin, DESIRED_TOTAL + 1):
            ways[coin_index] = ways[coin_index] + ways[coin_index - coin]

    answer = ways[DESIRED_TOTAL]
    print(answer)

if __name__ == '__main__':
  main()
