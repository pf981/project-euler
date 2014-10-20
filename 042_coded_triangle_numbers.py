def is_triangle(word):
    return True

def get_words():
    return []

def main():
    answer = sum(1 for word in get_words() if is_triangular(word))

    answer = 0
    print(answer)

if __name__ == '__main__':
    main()
