import itertools

def is_cube(n):
    return round(n**(1/3.0))**3 == n

def main():
    # for n in itertools.count(1):
    for n in range(345, 346):
        cube = n**3
        counts = sum(1
                     for permutation in set(itertools.permutations(str(cube)))
                     if is_cube(int(''.join(permutation))))

        # for s in set(''.join(l) for l in list(itertools.permutations(str(cube)))):
        #     print("@",s)

        for permutation in set(itertools.permutations(str(cube))):
            if is_cube(int(''.join(permutation))):
                print(''.join(permutation))

        print(counts)
        if counts == 3:
            answer = n # FIXME: This is not the answer
            break
    # print(answer)

if __name__ == '__main__':
    main()


# Alternative: Generate all cubes up to a point, sort digits and count them. Find the one with 5 permutations