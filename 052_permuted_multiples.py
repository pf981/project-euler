# This version is approximately three times faster than v1 just by using
#  sorted strings instead of counting lists. I would have thought it would be
#  more efficient to count as this is an O(1) operation but sorting is better
#  in this case.
import collections
import itertools

def are_permutations(int_list):
    """
    Returns true if all the elements of int_list are permutations of each
    other. False otherwise.
    """
    for i, num in enumerate(int_list):
        if i == 0:
            first_digits = collections.Counter(str(int(num)))
            continue

        digits = collections.Counter(str(int(num)))

        # If an element of the list has a different digit count to the first,
        # it is not a permutation
        if digits != first_digits:
            return False
    return True

def main():
    for num in itertools.count(1):
        if are_permutations([num, 2*num, 3*num, 4*num, 5*num, 6*num]):
            answer = num
            break

    print(answer)

if __name__ == '__main__':
  main()
