import sys

sys.stdin = open('input1.txt')

def check(num):
    global N, K, lines, max_line, max_length

    cnt = 0

    for i in range(N):
        cnt += lines[i] // num

    if cnt == K:
        if num > max_length:
            max_length = num
    
    if num < max_line:
        check(num + 1)

N, K = map(int, input().split())

lines = []

for _ in range(N):
    lines.append(int(input()))

max_length = 0

check(1)

print(max_length)