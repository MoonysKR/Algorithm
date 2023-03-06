import sys

sys.stdin = open('input1.txt')

sys.setrecursionlimit(10**6)

def check(num):
    global N, info, visited, lst

    # print(num)
    
    if visited[num] == 1:
        return
    
    visited[num] = 1
    lst.append(num + 1)

    for i in range(N):
        if info[num][i] == 1 and visited[i] == 0:
            check(i)



N, M = map(int, input().split())

info = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    start, end = map(int, input().split())

    info[start - 1][end - 1] = 1
    info[end - 1][start - 1] = 1

visited = [0 for _ in range(N)]

group = []


for i in range(N):
    if visited[i] == 0:
        lst = []
        check(i)
        # print(lst)
        group.append(lst)

print(len(group))