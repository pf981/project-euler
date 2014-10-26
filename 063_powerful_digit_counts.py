MAX_EXPONENT = 100
MAX_BASE = 100

def main():
    n_digit_and_nth_powers = []

    # For each exponent and base
    for n in range(1, MAX_EXPONENT):
        for base in range(1, MAX_BASE):
            # If base^n is n-digits
            if len(str(base ** n)) == n:
                n_digit_and_nth_powers.append(n)

    answer = len(n_digit_and_nth_powers)
    print(answer)

if __name__ == '__main__':
    main()
