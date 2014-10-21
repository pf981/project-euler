# This is a more efficient solution. All it does differently is it assumes the
# pandigital product always has length 4, which can be proven mathematically
# in the following way.
#
# The pandigital product must satisfy c such that a*b = c
# Assume there exists a and b, satisfying the requirements for the pandigital
# product equation such that c's length is greater than 4.
#
# Clearly a*b must be less than 99*99 = 9801, but a*b = c < 9801. But if
#c > 9801, this contradicts our assumption that c's length is greater than 4.
#
# Therefore, there must be no valid solution for c with length greater than
# 4. A similar proof can be done to prove c's length cannot be less than 4.
import itertools

def list_to_int(nums):
    return int(''.join(map(str, nums)))

def main():
    # This is just the RHS of a*b=c
    pandigital_products = set()

    for permutation in itertools.permutations(range(1, 10)):
        for i in range(1, len(permutation) - 4):
            # Assume the right hand side has width 4
            first = list_to_int(permutation[:i])
            second = list_to_int(permutation[i:-4])
            third = list_to_int(permutation[-4:])

            if first * second == third:
                print(first, "*", second, "=", third)
                pandigital_products.add(third)

    answer = sum(pandigital_products)
    print(answer)

if __name__ == '__main__':
  main()
