import sys

sys.stdin = open('input2.txt')

V, E = map(int, input().split())

def get_min_score(start, visited, visited_cnt, tmp_score):
    global maps, min_score, V, E

    print(start, visited, visited_cnt, tmp_score)
    if visited_cnt == V:
        if tmp_score < min_score:
            min_score = tmp_score
        return

    for i in range(len(routes[start])):
        end = routes[start][i]
        if visited[end] == 0:
            visited[end] = 1
            get_min_score(end, visited, visited_cnt + 1, tmp_score + maps[start][i])
            visited[end] = 0

maps = [[] for _ in range(V)]
routes = [[] for _ in range(V)]

# 예상 리스트 모양
# [[1, 2], [0], [0]]
# [[1000, 500], [1000], [500]]

for i in range(E):
    start, end, score = map(int, input().split())
    if routes[start - 1] == []:
        routes[start - 1].append(end - 1)
        maps[start - 1].append(score)
    else:
        for j in range(len(routes[start - 1])):
            if end - 1 in routes[start - 1]: 
                if maps[start - 1][j] > score:
                    maps[start - 1][j] = score
            elif end - 1 not in routes[start - 1]:
                routes[start - 1].append(end - 1)
                maps[start - 1].append(score)

for i in range(V):
    start = i
    for j in range(len(routes[i])):
        end = routes[i][j]
        if start not in routes[end]:
            routes[end].append(start)
            maps[end].append(maps[start][j])
        else:
            for k in range(len(routes[end])):
                if routes[end][k] == start:
                    if maps[end][k] > maps[start][j]:
                        maps[end][k] = maps[start][j]

visited = [0 for _ in range(V)]

visited[0] = 1

min_score = 2147483647 * V

get_min_score(0, visited, 1, 0)

print(min_score)