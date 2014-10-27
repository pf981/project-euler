import collections
import itertools
import re

def calculate_index_of_coincidence(text):
    N = len(text)
    counts = collections.Counter(text.lower())
    # print(counts)

    # for letter in range(ord('a'), ord('z') + 1):
    #     print(chr(letter), counts[chr(letter)])

    index_of_coincidence = 26/(N*(N-1)) * sum(counts[chr(letter)] * (counts[chr(letter)] - 1) for letter in range(ord('a'), ord('z') + 1))

    return index_of_coincidence

def xor_text(password, digits):
    result = []
    password_cycle = itertools.cycle(password)

    for digit in digits:
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

    # decrypted = xor_text([ord('g'), ord('o'), ord('d')], digits)
    # decrypted_string = ''.join(chr(s) for s in decrypted)
    # print(decrypted_string)
    # print(sum(decrypted))
    # return

    decrypted_strings = []

    for p1 in range(ord('a'), ord('z') + 1):
        for p2 in range(ord('a'), ord('z') + 1):
            for p3 in range(ord('a'), ord('z') + 1):
                password = [p1, p2, p3]
                password_string = ''.join(chr(p) for p in password)

                # print("@@", password_string)
                decrypted = xor_text(password, digits)
                decrypted_string = ''.join(chr(s) for s in decrypted)
                decrypted_strings.append(password_string + decrypted_string)
                # print(calculate_index_of_coincidence(decrypted_string))
                # if re.search("you", decrypted_string.lower()):
                #     print(password_string, decrypted_string[:30])

    decrypted_strings.sort(key=lambda x: x.count('and'))
    for d in decrypted_strings:
        print(d[:40])

    answer = 0
    print(answer)

if __name__ == '__main__':
    main()
