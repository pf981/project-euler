# Time:
# real    0m1.789s
# user    0m1.702s
# sys     0m0.082s
import sympy

def main():
    count = 0
    # Brute force all n and r
    for n in range(1, 101):
        for r in range(1, n+1):
            if sympy.binomial(n, r) > 1000000:
                count += 1
    answer = count
    print(answer)

if __name__ == '__main__':
    main()
