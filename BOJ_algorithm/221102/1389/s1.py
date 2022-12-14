import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

info = [[] for _ in range(N)]

# print(info)
# [[], [], [], [], []]

for i in range(M):
    j, k = map(int, input().split())
    info[j-1] += [k-1]
    # info[k-1] += [j-1]

# print(info)
# [[2, 3], [2], [0, 3, 1], [0, 4, 2], [3]]
# [[2, 3], [], [1], [4, 2], []]

shorts = [[0] * N for _ in range(N)]

# print(shorts)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(N):
    for j in range(N):
        if i == j:
            shorts[i][j] = -1
    for j in info[i]:
        shorts[i][int(j)] = 1
        shorts[j][int(i)] = 1
        
# print(shorts)
# [
# [-1, 0, 1, 1, 0],
# [0, -1, 1, 0, 0],
# [1, 1, -1, 1, 0],
# [1, 0, 1, -1, 1],
# [0, 0, 0, 1, -1]
# ]

# 공통으로 연결된 친구들은 +1 씩 해줄 예정

for a in range(6):
    for i in range(N):
        for j in range(N):
            if shorts[i][j] != 0 and i != j:
                for k in range(N):
                    if shorts[j][k] != 0 and j != k:
                        if shorts[i][k] == 0 or shorts[i][k] > shorts[j][k] + 1:
                            shorts[i][k] = shorts[j][k] + 1
                            shorts[k][i] = shorts[j][k] + 1

# print(shorts)
# [
# [-1, 2, 1, 1, 2],
# [2, -1, 1, 2, 2],
# [1, 1, -1, 1, 2],
# [1, 2, 1, -1, 1],
# [2, 2, 2, 1, -1]
# ]

results = [0 for _ in range(N)]

min_num = 6
min_person = 0

# print(results)
# [0, 0, 0, 0, 0]

for i in range(N):
    for j in range(N):
        results[i] += shorts[i][j]
    if results[i] < min_num:
        min_num = results[i]
        min_person = i + 1

print(min_person)