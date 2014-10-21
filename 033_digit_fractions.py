import fractions
from helpers import helpers

def cast_out(numerator, denominator):
    str_n = str(numerator)
    str_d = str(denominator)

    for n_index in range(2):
        for d_index in range(2):
            if str_n[n_index] == str_d[d_index]:
                # Return the fraction with the shared digit removed
                other_n_index = (n_index + 1) % 2
                other_d_index = (d_index + 1) % 2
                return fractions.Fraction(int(str_n[other_n_index]), int(str_d[other_d_index]))

    return None

def main():
    special_fractions = []
    for numerator in range(10, 100):
        # Discard trivial examples
        if numerator % 10 == 0:
            continue

        for denominator in range(numerator + 1, 100):
            # Discard trivial examples (and prevent division by 0)
            if denominator % 10 == 0:
                continue

            fraction = fractions.Fraction(numerator, denominator)
            casted = cast_out(numerator, denominator)
            if casted == fraction:
                special_fractions.append(fraction)

    answer = helpers.product(special_fractions).denominator
    print(answer)

if __name__ == '__main__':
  main()
