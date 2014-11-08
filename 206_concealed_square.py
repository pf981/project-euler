import re

# The answer must lie between sqrt(1020304050607080900) = 1010101010.1 and sqrt(1929394959697989990) = 1389026623.11
LOWER_BOUND = 1010101010
UPPER_BOUND = 1389026623

def main():
    # print(str(11223344556677889940))
    # print('1.2.3.4.5.6.7.8.9.0')
    # print(re.match('1.2.3.4.5.6.7.8.9.0', str(1122334455667788940)))
    # return


    for num in range(LOWER_BOUND, UPPER_BOUND+1):
        print(num)
        if re.match('1.2.3.4.5.6.7.8.9.0', str(num*num)):
            answer = num
            break

    print(answer)

if __name__ == '__main__':
    main()