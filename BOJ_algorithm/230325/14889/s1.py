import sys

sys.stdin = open('input1.txt')

N = int(input())

info = list(list(map(int, input().split())) for _ in range(N))

# print(*info, sep= '\n')
# [0, 1, 2, 3]
# [4, 0, 5, 6]
# [7, 1, 0, 2]
# [3, 4, 5, 0]

min_value = N * 100

# 퍼스트 팀은 첫번째, 나머지는 세컨팀이라 칭할 예정
# tmp_value는 여태 퍼스트 - 세컨드를 해온 값들의 합
def check(person, first_num, second_num, tmp_value):
    global N, info

    # 첫 팀이 다 차면
    if first_num == N // 2:
        for i in range(person, N):
            for j in range(i, N):
                tmp_value -= info[i][j] + info[j][i]
        if abs(tmp_value) < min_value:
            min_value = abs(tmp_value)
        return

    # 세컨 팀이 다 차면
    if second_num == N // 2:
        for i in range(person, N):
            for j in range(i, N):
                tmp_value += info[i][j] + info[j][i]
        if abs(tmp_value) < min_value:
            min_value = abs(tmp_value)
        return
    