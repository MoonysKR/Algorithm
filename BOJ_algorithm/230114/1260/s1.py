import sys

sys.stdin = open('input4.txt')

from collections import deque

def dfs(start):
    global info, dfs_visited

    if start + 1 in dfs_visited or len(dfs_visited) == N:
        return
    else:
        dfs_visited.append(start + 1)
        for i in range(len(info[start])):
            if info[start][i] == 1:
                dfs(i)


def bfs(info):
    global bfs_visited

    togo = deque()

    for i in range(len(info[V-1])):
        if info[V-1][i] == 1:
            togo.append((V-1, i))

    # print(togo)
    # deque([(2, 0), (2, 3)])

    while togo and len(bfs_visited) != N:
        # print(togo)

        start, end = togo.popleft()

        if len(bfs_visited) == 0:
            bfs_visited.append(start + 1)
        
        if end + 1 not in bfs_visited:
            bfs_visited.append(end + 1)
            for i in range(len(info[end])):
                if info[end][i] == 1: 
                    togo.append((end, i))


N, M, V = map(int, input().split())

info = [[0]* N for _ in range(N)]

for i in range(M):
    start, end = map(int, input().split())
    info[start-1][end-1] = 1
    info[end-1][start-1] = 1

# print(*info, sep='\n')

bfs_visited = [V]
dfs_visited = []

dfs(V-1)
print(*dfs_visited)
bfs(info)
print(*bfs_visited)
