def main():
    n = 1000
    primes = []
    ways = [0] * n
    ways[0] = 1
    for num in range(2, n):
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        
        if not is_prime:
            continue

        primes.append(num)
        for i in range(n - num):
            ways[i + num] += ways[i]
    
    for num, count in enumerate(ways):
        if count > 5000:
            answer = num
            break
    print(answer)
        

if __name__ == '__main__':
    main()
