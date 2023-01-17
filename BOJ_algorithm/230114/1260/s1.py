import sys

sys.stdin = open('input2.txt')

from collections import deque

N, M, V = map(int, input().split())

info = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    info[a-1].append(b-1)

for i in range(N):
    info[i] = sorted(info[i])

print(info)
# [[1, 2, 3], [3], [3], []]

visited_bfs = []
visited_dfs = []

def bfs(info):
    global visited_bfs

    que = deque()

    for i in range(len(info[V-1])):
        que.append((V-1, info[V-1][i]))

    # print(que)
    # deque([(2, 0), (2, 3)])

    while que and len(visited_bfs) < N:
        print(que)
        start, end = que.popleft()
        print(start, end)
        # 출발점이 방문한 지점에 없다면(처음 시작을 위한 로직) 방문 기록에 추가
        if start + 1 not in visited_bfs:
            visited_bfs.append(start + 1)
        
        # 출발점과 연결된 지점들을 순회하여 
        for i in range(len(info[start])):
            # 해당 지점이 방문 기록에 없다면, 방문 기록에 추가
            if info[start][i] + 1 not in visited_bfs:
                visited_bfs.append(info[start][i] + 1)
                # 방문점을 시작점으로 한 도착점 큐에 추가 
        for j in range(len(info[end])):
            print(len(info[end]))
            que.append((end, info[end][j]))
            print(end, info[end][j])
    
    # print(visited_bfs)
    
bfs(info)

print(visited_bfs)