import sys

sys.stdin = open('input3.txt')

n = int(input())

lst = list(map(int, input().split()))

max_sum = min(lst)

# 1개부터 n개의 연속된 수 파악

for i in range(n):
    for j in range(i + 1, n + 1):
        # print(lst[i:j])
        if sum(lst[i:j]) > max_sum:
            max_sum = sum(lst[i:j])


print(max_sum)