GRID_SIZE = 20

def right(pos):
    if pos[0] < GRID_SIZE:
        return (pos[0] + 1, pos[1])
    return

def down(pos):
    if pos[1] < GRID_SIZE:
        return (pos[0], pos[1] + 1)
    return

# FIXME: This reccursive solution is too inefficient
def count_routes_r(pos):
    if pos == (GRID_SIZE, GRID_SIZE):
        return 1
    return count_routes(right(pos) + down(pos))

def count_routes():
    routes = 0
    backtrack_stack = [(0, 0)]
    while backtrack_stack:
        pos = backtrack_stack.pop()

        # If this position came from an invalid move (out of bounds)
        if not pos:
            # Skip
            continue

        # If we are at the destination
        if pos == (GRID_SIZE, GRID_SIZE):
            # This is a valid route
            routes += 1
            continue

        # Attempt to go right and down
        backtrack_stack.append(right(pos))
        backtrack_stack.append(down(pos))
    return routes

def main():
    answer = count_routes()
    print(answer)

if __name__ == '__main__':
  main()
