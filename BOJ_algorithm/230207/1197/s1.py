# 문제
# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

# 입력
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

# 출력
# 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

import sys

sys.stdin = open('input1.txt')

def get_min_score(start, visited, visited_cnt, tmp_score):
    global maps, min_score, V, E

    if visited_cnt == V:
        if tmp_score < min_score:
            min_score = tmp_score
            return

    if tmp_score >= min_score:
        return


    for i in range(V):
        if routes[start][i] != 0 and visited[i] == 0:
            visited[i] = 1
            get_min_score(i, visited, visited_cnt + 1, tmp_score + maps[start][i])
            visited[i] = 0

V, E = map(int, input().split())

maps = [[0 for _ in range(V)] for _ in range(V)]

routes = [[0 for _ in range(V)] for _ in range(V)]

min_score = 2147483647 * V

for i in range(E):
    start, end, score = map(int, input().split())
    if routes[start - 1][end - 1] == 0:
        routes[start - 1][end - 1] = 1
        routes[end - 1][start - 1] = 1
        maps[start - 1][end - 1] = score
        maps[end - 1][start - 1] = score
    elif routes[start - 1][end - 1] == 1 and routes[start - 1][end - 1] > score:
        maps[start - 1][end - 1] = score
        maps[end - 1][start - 1] = score

# print(maps)

visited = [0 for _ in range(V)]

visited[0] = 1

get_min_score(0, visited, 1, 0)

print(min_score)