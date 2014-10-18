from scipy.misc import comb

GRID_SIZE = 20

def main():
    answer = comb(GRID_SIZE + GRID_SIZE, GRID_SIZE)
    print(answer)

if __name__ == '__main__':
  main()
