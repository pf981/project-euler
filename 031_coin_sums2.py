import collections
import prettytable

DESIRED_TOTAL = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def print_table(ways_to_form):
    header = ["<=" + str(coin) for coin in COINS]
    header = ["Target"] + header
    table = prettytable.PrettyTable(header)

    for target in range(10):
        row_data = [ways_to_form[target, coin_index] for coin_index, _ in enumerate(COINS)]
        table.add_row([target] + row_data)

    table.add_row(["..."]*9)

    for target in range(190, 201):
        row_data = [ways_to_form[target, coin_index] for coin_index, _ in enumerate(COINS)]
        table.add_row([target] + row_data)

    print(table)


def main():
    # ways_to_form[target, max_coin_index] is the number of possible ways to
    # form a total of target using coins whose index is less than
    # max_coin_index. For example ways_to_form[3, 3] == 2 because there are 2
    # ways to form a total of 3 using the coins 1, 2 and 5
    ways_to_form = collections.defaultdict(int)

    # There is exactly one way to form any target using only the 1p coin
    for target in range(DESIRED_TOTAL + 1):
        ways_to_form[target, 0] = 1

    for target in range(DESIRED_TOTAL + 1):
        for coin_index, coin in enumerate(COINS[1:], start=1):
            # If the coin cannot fit in the target
            if coin > target:
                # The ways to form will be no different than the ways to form
                # the target using the coins less than this one
                ways_to_form[target, coin_index] = ways_to_form[target, coin_index - 1]
            # If the coin can fit
            else:
                # It is the ways to form the target using coins less than this one
                ways_to_form[target, coin_index] = ways_to_form[target, coin_index - 1]

                # AND the number of ways when using this coin
                ways_to_form[target, coin_index] += ways_to_form[target - coin, coin_index]

    # Generate and print the table
    print("Ways to form target using coins lass than or equal to a value")
    print_table(ways_to_form)

    # The solution is the number of ways to form 200 using all the coins less
    # than or equal to 200
    answer = ways_to_form[DESIRED_TOTAL, len(COINS) - 1]
    print("Answer is", answer)


if __name__ == '__main__':
  main()
