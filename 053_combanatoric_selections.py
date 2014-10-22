import sympy

def main():
    count = 0
    # Brute force all n and r
    for n in range(1, 101):
        for r in range(1, n+1):
            if sympy.binomial(n, r) > 1000000:
                print(n, r)
                count += 1
    answer = count
    print(answer)

if __name__ == '__main__':
    main()
