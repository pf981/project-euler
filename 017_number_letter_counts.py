from helpers import helpers

UPPER = 1000

ONES_WORDS = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
    }

TENS_WORDS = {
    1: "", # This is counted in ones
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
    0: ""
    }




def letters(num):
    if num == 1000:
        return len("one") + len("thousand")

    total = 0

    # If we are dealing with 10-19
    if num >= 10 and int(str(num)[-2:-1]) == 1:
        total += len(ONES_WORDS[int(str(num)[-2:])])
    else:
        # Ones
        total += len(ONES_WORDS[int(str(num)[-1:])])

        if num < 10:
            return total

        # Tens
        total += len(TENS_WORDS[int(str(num)[-2:-1])])

    if num < 100:
        return total

    # Hundreds
    total += len(ONES_WORDS[int(str(num)[-3:-2])]) + len("hundred")

    # And?
    if int(str(num)[-2:]) > 0:
        total += len("and")

    return total


def int_to_words(num):
    """
    Returns a string representation of the number
    """
    if num == 1000:
        return "one thousand"

    words = ""

    # If we are dealing with 10-19
    if int(str(num)[-2:-1]) == 1:
        total += len(ONES_WORDS[int(str(num)[-2:])])
    else:
        # Ones
        words += ONES_WORDS[int(str(num)[-1:])]

        if num < 10:
            return words

         # Tens
        total += len(TENS_WORDS[int(str(num)[-2:-1])])

    if num < 100:
        return total

    # Hundreds
    total += len(ONES_WORDS[int(str(num)[-3:-2])]) + len("hundred")

    # And?
    if int(str(num)[-2:]) > 0:
        total += len("and")

    return total


def main():
#    for num in range(1, UPPER + 1):
#        print(int_to_words(num))

    answer = sum(letters(num) for num in range(1, UPPER + 1))
    print(answer)

if __name__ == '__main__':
  main()
