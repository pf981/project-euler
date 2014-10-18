def main():
    answer = 0;
    for num in fib():
        if num > 4000000:
            break
        if num % 2 == 0:
            answer += num
    print(answer)

def fib():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

if __name__ == '__main__':
  main()
