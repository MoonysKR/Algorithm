import sys

from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, input().split())

# print(N, M)

counts = [[0] * N for _ in range(N)]

# print(counts)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

info = [[] for _ in range(N)]  

for i in range(M):
    s, e = map(int, input().split())
    info[s-1].append(e-1)
    info[e-1].append(s-1)

# print(info)
# [[2, 3], [2], [0, 3, 1], [0, 4, 2], [3]]

for i in range(N):

    que = deque()
    for j in range(len(info[i])):
        que.append(info[i][j])
    cnt = 1

    # print(que)
    # deque([2, 3])
    # deque([2])
    # deque([0, 3, 1])
    # deque([0, 4, 2])
    # deque([3])

    while que:
        for k in range(len(que)):
            tmp = que.popleft()
            counts[i][tmp] = cnt
            for n in info[tmp]:
                if n != i and counts[i][n] == 0 and n not in que:
                    que.append(n)
        cnt += 1
        
# print(counts)
# [[0, 2, 1, 1, 2], [2, 0, 1, 2, 3], [1, 1, 0, 1, 2], [1, 2, 1, 0, 1], [2, 3, 2, 1, 0]]

results = []

for c in counts:
    tmp = 0
    for i in range(N):
        tmp += c[i]
    results.append(tmp)

print(results.index(min(results)) + 1)
