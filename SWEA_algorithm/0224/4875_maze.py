import sys

sys.stdin = open('4875_maze_input.txt')

T = int(input())

def maze(info):
    # 2의 위치를 찾기
    loc = [0, 0]
    for i in range(len(info)):
        for j in range(len(info)):
            if info[i][j] == 2:
                loc = [i, j]

    # 복사본 리스트 만들기
    loc_dup = info

    # 위치가 3이라면 return 1
    if info[loc[i]][loc[j]] == 3
        return 1

    # 위치가 3이 아닌데 주변에 0(길)이 있다면
    elif

    # 위치가 3이 아닌데 주변에 길도 없다면 0

for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input())) for _ in range(N)]

    # print(info)
    # [[1, 3, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 2, 1]]
    # [[1, 0, 0, 3, 1], [1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 2, 0, 0, 1]]
    # [[0, 0, 0, 1, 3], [0, 1, 1, 1, 0], [2, 1, 0, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

    # 함수를 만들자
    # 2의 위치를 받는 함수
    # 3이 나오면 return 1
    # 3이 안나오면 return 0
