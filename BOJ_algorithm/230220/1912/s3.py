import sys

sys.stdin = open('input3.txt')

n = int(input())

lst = list(map(int, input().split()))

tmp = 0

max_tmp = -1000

for i in range(n):
    tmp += lst[i]
    if tmp > max_tmp:
        max_tmp = tmp
    
    if tmp < 0:
        tmp = 0

print(max_tmp)