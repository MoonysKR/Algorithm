import sys

sys.stdin = open('1219_input.txt')


def way(s):
    global start, end, visited
    if s == end:
        start = 1
        return start
    if visited[s] == 0 and arr[s]:
        # print('s', s)
        visited[s] = 1
        for i in range(len(arr[s])):
            way(arr[s][i])


for i in range(1, 11):
    # tc // N == 간선 개수 // nums == 노드 정보
    tc, N = map(int, input().split())
    infos = list(map(int, input().split()))

    # 간선 정보 시작점(인덱스, 키) 도착점(밸류)
    # 99면 도착 98까지 정보 주어짐
    arr = [[] for _ in range(99)]

    for i in range(N):
        arr[infos[2*i]] += [infos[2*i+1]]

    # print(arr)
    # [[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], [], [], [], [], [], [], [], [], [], [],
    #  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
    #  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
    #  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    visited = [0] * 99

    start = 0
    end = 99

    way(0)

    print(f'#{tc} {start}')


