from helpers import helpers
# f(n) = n^2 + an + b
# Clearly, b must be prime as f(0) must be prime
# a must be b + p - 1 for some prime p (But this code doesn't use this fact)

MAX_PRIME = 40000
PRIMES = [p for p in helpers.get_million_primes()[:MAX_PRIME] if p < MAX_PRIME]

def chain(a, b):
    n = 0
    while n*n + a*n + b in PRIMES:
        n += 1

    return n

def main():
    best_chain = 0
    # b must be prime
    b_range = [p for p in PRIMES if p < 1000]
    # For each a, b combination
    for a in range(-1000, 1000):
        for b in b_range:
            cur_chain = chain(a, b)

            if cur_chain > best_chain:
                best_chain = cur_chain
                best_a = a
                best_b = b

    print(best_chain, best_a, best_b)
    answer = best_a * best_b
    print(answer)

if __name__ == '__main__':
    main()
