import itertools
import re

def xor_text(password, digits):
    result = []
    password_cycle = itertools.cycle(password)

    for digit in (ord(d) for d in digits):
        password_char = next(password_cycle)
        # print(chr(password_char))
        # print(password_copy[0])
        result.append(password_char ^ digit)
        # itertools.cycle(password_copy)


    # for digit in (ord(d) for d in digits):
    #     password_copy = next(password_cycle)
    #     # print(password_copy[0])
    #     result.append(password_copy[0] ^ digit)
    #     itertools.cycle(password_copy)

    return result



def main():
    with open("p059_cipher.txt") as in_file:
        text = in_file.read()

    digits = [int(digit) for digit in re.findall("(\d+)", text)]

    for p1 in range(ord('a'), ord('z') + 1):
        for p2 in range(ord('a'), ord('z') + 1):
            for p3 in range(ord('a'), ord('z') + 1):
                password = [p1, p2, p3]
                password_string = ''.join(chr(p) for p in password)

                print("@@", password_string)
                decrypted = xor_text(password, text[:20])
                print(''.join(chr(s) for s in decrypted))

    answer = 0
    print(answer)

if __name__ == '__main__':
    main()
