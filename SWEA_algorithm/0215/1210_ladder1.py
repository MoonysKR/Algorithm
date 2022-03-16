import sys

sys.stdin = open('1210_ladder_input.txt')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]


    # if문으로 2부터 찾아서 시작
    # pos로 위치 지정
    # 위로 이동 기본이지만
    # if문을 이용해 왼쪽이나 오른쪽에 길이 있다면 이동

    # 도착점 찾기
    for i in range(100):
        if ladder[99][i] == 2:
            pos = [99, i]

    # 도착점 왼쪽, 오른쪽 수색 및 위로 이동
    # 지나온 길 0으로 삭제 (오른쪽으로 왔다가 왼쪽으로 돌아 가는 것 방지)
    while pos[0] != 0:
        if 0 < pos[1] < 99:
            if ladder[pos[0]][pos[1]-1] == 1:
                ladder[pos[0]][pos[1]] = 0
                pos[1] -= 1
            elif ladder[pos[0]][pos[1]+1] == 1:
                ladder[pos[0]][pos[1]] = 0
                pos[1] += 1
            else:
                pos[0] -= 1
        if pos[1] == 0:
            if ladder[pos[0]][pos[1]+1] == 1:
                ladder[pos[0]][pos[1]] = 0
                pos[1] += 1
            else:
                pos[0] -= 1
        if pos[1] == 99:
            if ladder[pos[0]][pos[1]-1] == 1:
                ladder[pos[0]][pos[1]] = 0
                pos[1] -= 1
            else:
                pos[0] -= 1



    print(f'#{tc} {pos[1]}')