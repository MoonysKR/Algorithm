import sys

sys.stdin = open('5209_input.txt')

import copy

T = int(input())

# prdct에 fctry를 추가해주면서 할 예정
def mfg(p, f, cst, visited):
    global min_cst, N

    # 딥카피... 안하면 안되더라
    visit = copy.deepcopy(visited)

    # p == N >> 마지막 생산품의 공장까지 정해졌을 때
    # 비용 추가
    # 최소값 비교
    if p == N:
        cst += infos[p][f]
        if cst < min_cst:
            min_cst = cst

    # 중간에라도 비용이 최소값을 초과하면 볼필요 없음
    if cst > min_cst:
        return

    # 아직 마지막 노드에 도착 못했을 경우,
    # 입력받은 p,f 값 비용에 추가
    # 방문기록 작성
    # 방문기록이 없는
    # 다음 p값에 해당하는 모든 f값에 보냄
    if p < N:
        cst += infos[p][f]
        for i in range(N+1):
            visit[i][f] = 1
        # print(p, f, visit)
        for i in range(1, N+1):
            if visit[p][i] != 1:
                mfg(p+1, i, cst, visit)



for tc in range(1, T + 1):
    # N개 공장 N개 물품
    N = int(input())
    infos = [[0] * (N+1)] +[[0] + list(map(int, input().split())) for _ in range(N)]
    # print(infos)
    # [[0, 0, 0, 0],
    # [0, 73, 21, 21],
    # [0, 11, 59, 40],
    # [0, 24, 31, 83]]

    min_cst = 99 * N

    # 방문기록 작성
    visited = [[0] * (N+1) for _ in range(N+1)]

    mfg(0, 0, 0, visited)

    print(f'#{tc} {min_cst}')
    # 1 63
    # 2 78
    # 3 129