import sys

sys.stdin = open('5251_input.txt')


def find(s, cnt):
    global ways, end, min_cnt
    if s == end:
        if cnt < min_cnt:
            min_cnt = cnt
            return

    if cnt >= min_cnt:
        return

    for way in ways[s]:
        # find(way[0], cnt + way[1])로 퉁칠 수 있음
        # print(way)
        cnt += way[1]
        # print(way[0], cnt)
        find(way[0], cnt)
        cnt -= way[1]

T = int(input())

for tc in range(1, T + 1):
    # 마지막 연결 지점 번호 == N // 도로의 개수 E
    N, E = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(E)]

    # print(infos)
    # [[0, 1, 1], [0, 2, 6], [1, 2, 1]]

    ways = [[] for _ in range(N)]
    for info in infos:
        ways[info[0]] += [[info[1], info[2]]]
    # print(ways)
    # [[[1, 1], [2, 6]], [[2, 1]]]

    start = 0
    end = N
    min_cnt = 10 * N
    cnt = 0

    find(start, cnt)

    print(f'#{tc} {min_cnt}')