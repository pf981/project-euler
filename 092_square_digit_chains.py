MAX_RANGE = 10000000

def generate_digit_squares(n):
    """
    Generates an infinite chain of sum of squares of the digits
    """
    chain_element = n
    while True:
        yield chain_element

        # The next element is the sum of the squares of the digits of the
        # current element
        chain_element = sum(int(digit) ** 2 for digit in str(chain_element))

def main():
    # These are the sets of numbers we know will arrive at 89 or 1
    numbers_arriving_at_89 = {89}
    numbers_arriving_at_1 = {1}

    for n in range(1, MAX_RANGE):
        print(n)
        # current_chain is the set of numbers which we are currently trying to
        # find where they lead. When we know that they lead to either 89 or 1,
        # then we know every element leads to that same number
        current_chain = set()

        # For each element in this chain
        for chain_element in generate_digit_squares(n):
            # If it is an element known to lead to 1
            if chain_element in numbers_arriving_at_1:
                # Then every element of this chain must lead to 1
                numbers_arriving_at_1 |= current_chain
                break

            # If it is an element known to lead to 89
            if chain_element in numbers_arriving_at_89:
                # Then every element of this chain must lead to 89
                numbers_arriving_at_89 |= current_chain
                break

            current_chain.add(chain_element)

    answer = len(numbers_arriving_at_89)
    print(answer)

if __name__ == '__main__':
    main()
