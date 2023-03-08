import sys

sys.stdin = open('input1.txt')

from collections import deque

N, M = map(int, input().split())

info = [[] for _ in range(N)]

for i in range(M):
    start, end = map(int, input().split())

    info[start - 1].append(end-1)
    info[end - 1].append(start-1)

# print(info)

visited = [0 for _ in range(N)]

cnt = 0

for i in range(N):
    if visited[i] == 0:
        que = deque()
        que.append(i)
        visited[i] = 1

        while que:

            start = que.popleft()
            # print(start)


            for end in info[start]:
                    if visited[end] == 0:
                        visited[end] = 1
                        que.append(end)

        cnt += 1


print(cnt)