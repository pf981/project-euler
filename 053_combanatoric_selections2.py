# This solution is approximately 2.75x faster than the previous brute force
# solution. This solution uses pascals triangle
# 1
# 1 1
# 1 2 1
# We can see that binomial(2, 2) = 2
#
# Time:
# real    0m0.651s
# user    0m0.559s
# sys     0m0.091s
import sympy
from scipy.linalg import pascal

def main():
    count = 0
    pascals_triangle = pascal(101, kind="lower")

    for n in range(101):
        for r in range(n+1):
            # binomial(n, r) is just pascals_triangle[n, r]
            if pascals_triangle[n, r] > 1000000:
                count += 1

    answer = count
    print(answer)

if __name__ == '__main__':
    main()
