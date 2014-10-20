import collections

DESIRED_TOTAL = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

# Defaults dictionary

def generate_coin_combinations(total):
    """
    Generates lists of coin combinations
    """
    current_combination = collections.defaultdict(int)

    current_sum = 0
    backtrack_stack = [COINS[0]] # Start by adding one pence
    while backtrack_stack:
        coin = backtrack_stack.pop()

        # If this coin makes the total too big
        if coin + current_sum > DESIRED_TOTAL:
            # Don't add it
            continue

        # Include the coin
        current_combination[coin] += 1
        current_sum += coin

        # If we are at the desired total
        if current_sum == DESIRED_TOTAL:
#            print(current_combination.values())
#            print(sum(current_combination.values())
            # This is a valid combination
            yield current_combination

            # Continue backtracking
            current_sum -= coin

        # Attempt to add other coins
        for new_coin in COINS:
            backtrack_stack.append(new_coin)
#        backtrack_stack.append(right(pos))
#        backtrack_stack.append(down(pos))
    return routes


def main():
#    coin_combinations = list(generate_coin_combinations(DESIRED_TOTAL))
    # coin_combinations = list(generate_coin_combinations(DESIRED_TOTAL))
    # print(coin_combinations)
    for combination in generate_coin_combinations(DESIRED_TOTAL):
        print(combination, sum(coin * value for coin, value in combination.items()))
    # answer = len(coin_combinations)
    # print(answer)


if __name__ == '__main__':
    main()
