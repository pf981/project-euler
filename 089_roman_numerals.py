import re
# 1000 M
# 900 CM
# 500 D
# 400 CD
# 100 C
# 90 XC
# 50 L
# 40 XL
# 10 X
# 9 IX
# 5 V
# 4 IV
# 1 I
value = {}
value['M'] = 1000
value['CM'] = 900
value['D'] = 500
value['CD'] = 400
value['C'] = 100
value['XC'] = 90
value['L'] = 50
value['XL'] = 40
value['X'] = 10
value['IX'] = 9
value['V'] = 5
value['IV'] = 4
value['I'] = 1

# There is probably a way to simplify the given roman numaral that doesn't
# involve finding the decimal representation

# Note that this doesn't put the characters in the correct order, it just does
# the substitutions. The correct order is not needed as we are only interested
# in counting how many characters there are
# def simplify_roman(original):
#     fixed = re.sub(r'IIII', 'IV', original)
#     fixed = re.sub(r'VIV', 'IX', fixed)
#     fixed = re.sub(r'XXXX', 'XL', fixed)
#     fixed = re.sub(r'LXL', 'XC', fixed)
#     fixed = re.sub(r'CCCC', 'CD', fixed)
#     fixed = re.sub(r'DCD', 'CM', fixed)
#     return fixed

def roman_to_int(roman):
    total_value = 0
    prev_value = 0

    for letter in reversed(roman):
        # print(i, letter, reversed_roman[i-1])

        # If this number is less than it's predescessor (reversed)
        if value[letter] >= prev_value:
            total_value += value[letter]
        else:
            total_value -= value[letter]

        prev_value = value[letter]
        print(letter, value[letter], total_value)
    return total_value
# def roman_to_int(roman):
#     reversed_roman = roman[::-1]
#     cur_value = 0
#     prev_value = None
#     for i, letter in enumerate(reversed_roman):
#         # print(i, letter, reversed_roman[i-1])

#         # If this number is less than it's predescessor (reversed)
#         if value[letter] < value[reversed_roman[i-1]]:
#             cur_value -= value[letter]
#         else:
#             cur_value += value[letter]
#         print(letter, value[letter], cur_value)
#     return cur_value

def simplify_roman(original):
    fixed = roman_to_int(original)
    return fixed

def test(original, expected):
    if (simplify_roman(original) == expected):
        print(original, "passed")
    else:
        print(original, "FAILED")
        print("Expected:", expected)
        print("Got:     ", simplify_roman(original))
        print()

def unit_tests():
    print(roman_to_int("MMMCDLXXXVII") == 3487)
    print(roman_to_int("MMMCDLXXXVII"))
    test("MMMCDLXXXVII", "MMMDLXXXVII")

def main():
    unit_tests()
    return
    roman_numerals = re.findall("(\w+)", open("p089_roman.txt").read())
    for original, simplified in ((roman_numeral, simplify_roman(roman_numeral)) for roman_numeral in roman_numerals):
        print(original, simplified)
    answer = sum(len(simplify_roman(roman_numeral) )
                 for roman_numeral in roman_numerals)
    print(answer)
    # print(roman_numerals)
    # print(simplify_roman("MMMDLXVIIII"))
    # print(simplify_roman("XXXXVIIII"))

if __name__ == '__main__':
    main()