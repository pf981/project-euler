import sympy

MAX_N = 1000000

def tot(n):
    return sympy.ntheory.totient(n)

def main():
    # for n in range(1, MAX_N + 1):
    #     pass
    answer = max((n for n in range(1, MAX_N + 1)), key=lambda x:x/tot(x))
    print(answer)

# yasnippit: type "ifmain" then tab to complete
if __name__ == '__main__':
    main()