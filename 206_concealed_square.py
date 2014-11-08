import itertools
import math

# The answer must lie between sqrt(1020304050607080900) = 1010101010.1 and sqrt(1929394959697989990) = 1389026623.11
LOWER_BOUND = 1010101010
UPPER_BOUND = 1389026623

# 9_0
# (a + b)^2 = a^2 + ab + b^2

def is_square(num):
    root = math.sqrt(num)
    return root == int(root)

def main():
    # print(is_square(25))
    # print(is_square(24))
    # for num in range(100):
    #     print(num, num*num)
    # return
    # for num in range(LOWER_BOUND, UPPER_BOUND+1):
    #     print(num)
    #     if re.match('1.2.3.4.5.6.7.8.9.0', str(num*num)):
    #         answer = num
    #         break

    # for num in range(LOWER_BOUND, UPPER_BOUND+1):
    #     print(num)
    #     if re.match('1.2.3.4.5.6.7.8.9.0', str(num*num)):
    #         answer = num
    #         break

    # Maybe would be quicker if reversed range
    # Generate all the in-between numbers that go in the gaps
    for in_betweens in range(10**11):
        print(str(in_betweens).zfill(10))
        # When splicing 1234567890 and the in-betweens, ensure that leading
        # zeros are kept
        candidate_square_list = list(zip("1234567890", str(in_betweens).zfill(10)))

        # Flatten the list of tuples of strings into an int
        candidate_square = int(''.join(itertools.chain(*candidate_square_list)))


        if is_square(candidate_square):
            answer = math.sqrt(candidate_square)
            break

    print(answer)

if __name__ == '__main__':
    main()