import itertools

def main():
    # for n in itertools.count(1):
    for n in range(345, 346):
        cube = sorted(str(n**3))
        print(cube)
        for permutation in itertools.permutations(str(n)):
            print(''.join(permutation), (int(''.join(permutation))**3))
            if cube == sorted(str(int(''.join(permutation))**3)):
                print(int(''.join(permutation)))
        counts = sum(1
                     for permutation in itertools.permutations(str(n))
                     if cube == sorted(str(int(''.join(permutation))**3)))
        print(counts)
        if counts == 3:
            answer = n # FIXME: This is not the answer
            break
    print(answer)

if __name__ == '__main__':
    main()