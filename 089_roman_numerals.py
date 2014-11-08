import re
value = {}
value['M'] = 1000
value['D'] = 500
value['C'] = 100
value['L'] = 50
value['X'] = 10
value['V'] = 5
value['I'] = 1

def roman_to_int(roman):
    total_value = 0
    prev_value = 0

    for letter in reversed(roman):
        # If this number is >= it's predescessor (reversed)
        if value[letter] >= prev_value:
            total_value += value[letter]
        else:
            total_value -= value[letter]

        prev_value = value[letter]
    return total_value

def int_to_roman(num):
    pass

def simplify_roman(original):
    return int_to_roman(roman_to_int(original))

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