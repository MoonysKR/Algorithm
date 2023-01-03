import sys

sys.stdin = open('input2.txt')

# N으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합을 구하는 프로그램을 작성하시오. 예를 들어 N=3일 때, 나머지와 몫이 모두 같은 자연수는 4와 8 두 개가 있으므로, 그 합은 12이다.

N = int(input())

result = 0

for i in range(1, N):
    tmp = i + (i * N)
    result += tmp

print(result)