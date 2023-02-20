import sys

sys.stdin = open('input3.txt')

n = int(input())

lst = list(map(int, input().split()))

idx = 1

max_sum = min(lst)

# 1개부터 n개의 연속된 수 파악
while idx < n + 1:

    for i in range(n - idx + 1):
        if sum(lst[i:i+idx]) > max_sum:
            max_sum = sum(lst[i:i+idx])
    
    idx += 1


print(max_sum)