import re

# Note that this doesn't put the characters in the correct order, it just does
# the substitutions. The correct order is not needed as we are only interested
# in counting how many characters there are
def simplify_roman(original):
    fixed = re.sub(r'IIII', 'IV', original)
    fixed = re.sub(r'VIV', 'IX', fixed)
    fixed = re.sub(r'XXXX', 'XL', fixed)
    fixed = re.sub(r'LXL', 'XC', fixed)
    fixed = re.sub(r'CCCC', 'CD', fixed)
    fixed = re.sub(r'DCD', 'CM', fixed)
    return fixed

def main():
    roman_numerals = re.findall("(\w+)", open("p089_roman.txt").read())

    answer = sum(len(roman_numeral) - len(simplify_roman(roman_numeral))
                 for roman_numeral in roman_numerals)
    print(answer)

if __name__ == '__main__':
    main()