import re

values = {}
values['M'] = 1000
values['D'] = 500
values['C'] = 100
values['L'] = 50
values['X'] = 10
values['V'] = 5
values['I'] = 1
letters = {}
letters[1000] = 'M'
letters[900] = 'CM'
letters[500] = 'D'
letters[400] = 'CD'
letters[100] = 'C'
letters[90] = 'XC'
letters[50] = 'L'
letters[40] = 'XL'
letters[10] = 'X'
letters[9] = 'IX'
letters[5] = 'V'
letters[4] = 'IV'
letters[1] = 'I'

def roman_to_int(roman):
    total_values = 0
    prev_values = 0

    for character in reversed(roman):
        # If this number is >= it's predescessor (reversed)
        if values[character] >= prev_values:
            total_values += values[character]
        else:
            total_values -= values[character]

        prev_values = values[character]
    return total_values

def int_to_roman(num):
    roman_numeral = ''

    # Put in all 1000s, then 900s then 500s then 400s etc.
    for value, letter in sorted(letters.items(), key=lambda x: x[0], reverse=True):
        # print(letter, value)
        while num >= value:
            # print(letter)
            roman_numeral += letter
            num -= value

    return roman_numeral

def simplify_roman(original):
    return int_to_roman(roman_to_int(original))

def test(original, expected):
    if (simplify_roman(original) == expected):
        print(original, "passed")
    else:
        print("FAILED:  ", original)
        print("Expected:", expected)
        print("Got:     ", simplify_roman(original))
        print()

def unit_tests():
    print(roman_to_int("MMMCDLXXXVII") == 3487)
    print(roman_to_int("MMMCDLXXXVII"))
    print(int_to_roman(3487))
    test("MMMCDLXXXVII", "MMMDLXXXVII")

def main():
    unit_tests()
    return

    roman_numerals = re.findall("(\w+)", open("p089_roman.txt").read())
    # for original, simplified in ((roman_numeral, simplify_roman(roman_numeral)) for roman_numeral in roman_numerals):
        # print(original, simplified)
    answer = sum(len(simplify_roman(roman_numeral) )
                 for roman_numeral in roman_numerals)
    print(answer)

if __name__ == '__main__':
    main()