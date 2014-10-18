def main():
  answer = sum(x for x in range(1000) if x % 3 == 0)
  answer += sum(x for x in range(1000) if x % 5 == 0)
  print(answer)


if __name__ == '__main__':
  main()
