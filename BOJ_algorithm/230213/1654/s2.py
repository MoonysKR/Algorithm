import sys

sys.stdin = open('input1.txt')

def check(start, end):
    global N, K, lines, max_length

    tmp = 0

    for i in range(N):
        tmp += lines[i] // start
    
    if tmp < K:
        return

    if (start + end) % 2 == 0:
        center = (start + end) // 2
    else:
        center = (start + end) // 2 + 1

    cnt = 0
    
    for i in range(N):
        cnt += lines[i] // center

    if cnt == K:
        if max_length < center:
            max_length = center
            check(center + 1, end)

    elif cnt > K:
        check(center + 1, end)

    elif cnt < K:
        check(start, center - 1)
    
N, K = map(int, input().split())

lines = []

for _ in range(N):
    lines.append(int(input()))

max_length = 0

start = 1
end = max(lines)
center = end // 2

check(start, end)

print(max_length)