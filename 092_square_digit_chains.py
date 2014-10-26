MAX_RANGE = 100

def generate_digit_squares(n):
    chain_element = n
    while True:
        yield chain_element

        # The next element is the sum of the squares of the digits of the
        # current element
        chain_element = sum(int(digit) ** 2 for digit in str(chain_element))

def main():
    numbers_arriving_at_89 = {89}
    numbers_arriving_at_1 = {1}

    for n in range(1, MAX_RANGE):
        current_chain = set()

        for chain_element in generate_digit_squares(n):
            print(chain_element)
            current_chain.add(chain_element)

            if chain_element in numbers_arriving_at_1:
                numbers_arriving_at_1 |= current_chain
                break

            if chain_element in numbers_arriving_at_89:
                numbers_arriving_at_89 |= current_chain
                break



    answer = len(numbers_arriving_at_89)
    print(answer)

if __name__ == '__main__':
    main()
