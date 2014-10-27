
def main():
    diagonals = []
    cur_value = 1
    for spiral_radius in range(1, 3):
        gap_between_diagonals = 2 * spiral_radius

        # Top right
        cur_value += gap_between_diagonals
        diagonals.append(cur_value)

        # Top left
        cur_value += gap_between_diagonals
        diagonals.append(cur_value)

        # Bottom left
        cur_value += gap_between_diagonals
        diagonals.append(cur_value)

        # Bottom right
        cur_value += gap_between_diagonals
        diagonals.append(cur_value)


    print(diagonals)

    answer = 0
    print(answer)


if __name__ == '__main__':
    main()
