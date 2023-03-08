import sys

sys.setrecursionlimit(10**9)

def check(num):
    global N, info, visited, lst

    # print(info)
    # print(lst)
    # print(num)

    
    if visited[num] == 1:
        return
    
    visited[num] = 1
    lst.append(num)

    for i in range(len(info[num])):
        if visited[info[num][i]] == 0:
            check(info[num][i])



N, M = map(int, input().split())

info = [[] for _ in range(N)]

for i in range(M):
    start, end = map(int, input().split())

    info[start - 1].append(end-1)
    info[end - 1].append(start-1)

# print(info)

visited = [0 for _ in range(N)]

group = []


for i in range(N):
    if visited[i] == 0:
        lst = []
        check(i)
        # print(lst)
        group.append(lst)

print(len(group))