def main():
    target = 100
    num_ways = [0] * (target + 1)

    # There is one way to make 0 as the sum of integers
    # (Note that we do not restrict to a minimum of two integers)
    num_ways[0] = 1

    for i in range(1, target+1):
        for cur_target in range(i, target + 1):
            # Compute the ways to make the current target based of the
            # previously computed values
            num_ways[cur_target] += num_ways[cur_target - i];

    # num_ways[target] is the number of ways to make the target as the sum of
    # integers. Subtract 1 to remove the case of just 1 integer in the
    # summation (sum(100) == 100)
    answer = num_ways[target] - 1
    print(answer)

if __name__ == '__main__':
    main()