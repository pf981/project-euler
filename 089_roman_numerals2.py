import re

# Note that this doesn't put the characters in the correct order, it just does
# the substitutions. The correct order is not needed as we are only interested
# in counting how many characters there are
def simplify_roman(original):
    substitutions = ((r'IIII', 'IV'), (r'VIV', 'IX'), (r'XXXX', 'XL'),
                     (r'LXL', 'XC'), (r'CCCC', 'CD'), (r'DCD', 'CM'))

    for regex, replace in substitutions: original = re.sub(regex, replace,
        original)

    return original

def main():
    roman_numerals = re.findall("(\w+)", open("p089_roman.txt").read())

    answer = sum(len(roman_numeral) - len(simplify_roman(roman_numeral))
                 for roman_numeral in roman_numerals)
    print(answer)

if __name__ == '__main__':
    main()