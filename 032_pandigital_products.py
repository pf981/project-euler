import itertools

def list_to_int(nums):
    return int(''.join(map(str, nums)))

def main():
    # This is just the RHS of a*b=c
    pandigital_products = set()

    for permutation in itertools.permutations(range(1, 10)):
        for i in range(1, len(permutation) - 2):
            for j in range(i + 1, len(permutation) - 1):
                first = list_to_int(permutation[:i])
                second = list_to_int(permutation[i:j])
                third = list_to_int(permutation[j:])

                if first * second == third:
                    print(first, "*", second, "=", third)
                    pandigital_products.add(third)

    answer = sum(pandigital_products)
    print(answer)

if __name__ == '__main__':
  main()
