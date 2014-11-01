# This solution is broken. I have kept it here just for reference. To see my proper solution, see 081_path_sum_two_ways3.py
import sys
import numpy as np

MATRIX = np.array([[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 736, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]])

# This is the same code as 018
def length_of_shortest_path(tree):
    """
    Returns the length of the shortest path through a tree where you can only
    traverse down or to the left
    """
    for row in reversed(range(len(tree) - 1)):
        print(row)
        for col in range(len(tree[row])):

            try:
                # Down
                parent1 = tree[row + 1][col]
            except IndexError:
                parent1 = None

            try:
                # Right
                parent2 = tree[row][col + 1]
            except IndexError:
                parent2 = None

            if parent1 != None and parent2 != None:
                print("AA")
                tree[row][col] += min(parent1, parent2)
            elif parent1 == None and parent2 != None:
                print("NA")
                tree[row][col] += parent2
            elif parent1 != None and parent2 == None:
                print("AN")
                tree[row][col] += parent1

            print('@', row, col, tree[row][col])
            for x in tree:
                print(x)


             # parent1 = tree.get()
 #            tree[row][col] += min(parent1, parent2)
             # tree[row][col] += min(i for i in [parent1, parent2] if i != None)
             # tree[row][col] += min(tree[row + 1][col], tree[row + 1][col + 1])

    return tree[0][0]

     # def length_of_shortest_path(tree):
     # """
     # Returns the length of the shortest path through a tree where you can only
     # traverse down or to the left
     # """
     # for row in reversed(range(len(tree) - 1)):
     #     print(row)
     #     for col in range(len(tree[row])):
     #         tree[row][col] += min(tree[row + 1][col], tree[row + 1][col + 1])

     # return tree[0][0]



def main():
    # print(MATRIX)

      # diags = [MATRIX[::-1,:].diagonal(i) for i in range(-MATRIX.shape[0]+1, MATRIX.shape[1])]
     # diags = 0


    diags = [MATRIX[::-1,:].diagonal(i).copy() for i in range(-MATRIX.shape[0]+1, MATRIX.shape[1] // 2 - 1)]
    diags2 = [MATRIX[::,::-1].diagonal(i).copy() for i in range(-MATRIX.shape[0]+1, MATRIX.shape[1] // 2 - 2)]

    all_diags = [MATRIX[::-1,:].diagonal(i).copy() for i in range(-MATRIX.shape[0]+1, MATRIX.shape[1])]

      # print(diags2)
      # print()
      # print()
      # diags = [MATRIX[::-1,:].diagonal(i) for i in range(-MATRIX.shape[0]+1, MATRIX.shape[1] // 2)]

      # diags = [MATRIX.diagonal(i) for i in range(-MATRIX.shape[0]+1,MATRIX.shape[1])]

  # Now back to the original array to get the upper-left-to-lower-right diagonals,
      # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
      # diags.extend(MATRIX.diagonal(i) for i in range(MATRIX.shape[1]-1,-MATRIX.shape[0],-1))

      # print(diags)


    for row in diags:
        print(row)
    for row in diags2:
        print(row)
    print()
    print()
    for row in all_diags:
        print(row)

     # answer = length_of_shortest_path(diags) + length_of_shortest_path(diags2)
    answer = length_of_shortest_path(all_diags)

    # for row in reversed(len(MATRIX) - 1):
                 #     for col in range(len(MATRIX[row])):
                 #         MARTIX[row][col] += max(tree[row + 1][col], tree[row + 1][col + 1])

    # FOR EACH / DIAGONAL
                 #    UPDATE IT
                 #        THe bottom right corner is the answer!


    print(answer)

if __name__ == '__main__':
  main()
