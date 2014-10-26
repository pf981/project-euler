import itertools

def isPenthagonal(num):
    n = ((num * 24 + 1)**0.5 + 1) / 6
    return n == int(n)

def get_min_distance():
    # pentagonals is the set of pentagonals that were previously generated
    pentagonals = set()

    # For every pentagonal
    for pentagonal in (n * (3 * n - 1) // 2 for n in itertools.count(1)):
        for pentagonal2 in pentagonals:
            # If the sum and difference are pentagonal
            # Note that we would have generated the difference, but not the
            # sum as it would be bigger than the current pentagonal
            if pentagonal - pentagonal2 in pentagonals and isPenthagonal(pentagonal + pentagonal2):
                # Return the distance
                return pentagonal - pentagonal2

        # Update the list of pentagonals
        pentagonals.add(pentagonal)

def main():
    answer = get_min_distance()
    print(answer)

if __name__ == '__main__':
    main()
