import re

#50


def is_triangular(word):
    sum_of_chars = sum(ord(ch) - ord('a') + 1 for ch in word.lower())
    print(sum_of_chars)

def get_words():
    with open("p042_words.txt") as in_file:
        text = in_file.read()
        return re.findall("\w+", text)

def main():
    triangular_numbers = [int(0.5 * n * (n + 1)) for n in range(500)]
    print(triangular_numbers)

#    is_triangular("SKY")

#    answer =0
    # answer = sum(1 for word in get_words() if is_triangular(word))
#    print(answer)

if __name__ == '__main__':
    main()
