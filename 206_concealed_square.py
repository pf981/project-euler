# This was my first attempt at this problem and it used brute force. It works,
# but takes several minutes to complete. A more efficient version is in
# 206_concealed_square2.py
import itertools
import math

# The answer must lie between sqrt(1020304050607080900) = 1010101010.1 and sqrt(1929394959697989990) = 1389026623.11
LOWER_BOUND = 1010101010
UPPER_BOUND = 1389026623

def is_square(num):
    root = math.sqrt(num)
    return root == int(root)

def main():
    ## This was my first attempt which searched for all candidates
    # for num in range(LOWER_BOUND, UPPER_BOUND+1):
    #     print(num)
    #     if re.match('1.2.3.4.5.6.7.8.9.0', str(num*num)):
    #         answer = num
    #         break
    # print(answer)
    # return

    ## This is my second attempt which searched for all squares
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