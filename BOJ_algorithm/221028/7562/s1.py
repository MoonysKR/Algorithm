# 문제
# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    L = int(input())
    now_x, now_y = list(map(int, input().split()))
    togo_x, togo_y = list(map(int, input().split()))

    maps = [[0] * L for i in range(L)]

    # print(maps)

    how_many = 0

    maps[now_y][now_x] = 1
    maps[togo_y][togo_x] = -1

    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]

    lst = [(now_x, now_y)]

    flag = 0

    while maps[now_y][now_x] != -1 and flag != 1:
        now_x, now_y = lst.pop(0)
        for i in range(8):
            if 0 <= now_y + dy[i] <= L-1 and 0 <= now_x + dx[i] <= L-1:
                new_y = now_y + dy[i]
                new_x = now_x + dx[i]
                if maps[new_y][new_x] == -1:
                    how_many = maps[now_y][now_x]
                    flag = 1
                    break
                elif maps[new_y][new_x] != 0:
                    pass
                else:
                    maps[new_y][new_x] = maps[now_y][now_x] + 1
                    lst.append((new_x, new_y))



    print(how_many)