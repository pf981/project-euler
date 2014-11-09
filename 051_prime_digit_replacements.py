# This is a mess and doesn't work. See the proper solution in 051_prime_digit_replacements2.py
# from sympy import sieve
import itertools
import re
import sympy

def any_length_combinations(l):
    # combinations = []
    # for i in range(len(l)):
    #     combinations += itertools.combinations(l, i+1)
    # return combinations[:-1]
    return itertools.combinations(l, 3)

def main():
    # print(re.match(r"4(.)\1", "433"))
    # print(re.match(r"4(.)\1{1}", "433"))
    # print(re.match(r"4(.)\1", "433"))
    # print(re.match(r"(.)\g<1>", "334"))
    # return
    # For each possible length digit
    # digits = 1
    digits = 6
    while(True):
        print("Generating", digits, "digit primes")

        # Generate the primes of that digit length
        primes = list(sympy.sieve.primerange(10**(digits-1), 10**digits))

        print("Finished generating")

        # Get all combinations of which indexes to keep
        combinations = list(any_length_combinations(range(digits)))
        print(combinations)
        # test = ["(.)", "\\0"]
        # print("".join(test))
        # return
        used_regex = set()
        for candidate in primes:
            print("Candidate:", candidate)
            for combination in combinations:
                # print("Trying combination", combination)
                matches = []

                # This is the regex that will make all the indexes in combination wildcards
                regex = list(str(candidate))
                regex[combination[0]] = "(.)"
                for i in combination[1:]:
                    regex[i] = '\\1{1}'
                regex = "".join(regex)

                if regex in used_regex:
                    continue
                used_regex.add(regex)

                for prime in primes:
                    if re.match(regex, str(prime)):
                        matches.append(prime)

                # print(candidate, regex, matches)
                if len(matches) >= 8:
                    print("FOUND", candidate, regex, matches)
                    return

        # Or just get all combinations of [0, 1, 2]. E.g. [0, 2] means you only keep the first and third digit
        # for prime in primes:
        #     max_mask = 0b111
        #     for mask in range(0b1, max_mask):
        #         print(bin(mask))

        digits += 1
        # if digits == 4:
        #     break

if __name__ == '__main__':
    main()