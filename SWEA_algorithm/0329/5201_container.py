import sys

sys.stdin = open('5201_input.txt')

T= int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))

    T_info = []

    for truck in T:
        truck_info = []
        for w in W:
            if truck >= w:
               truck_info += [w]
        T_info += [truck_info]

    # print(T_info)
    # [[2, 12, 13, 11], [2], [2], [2, 12, 13, 11, 18], [2], [2], [2], [2], [2, 12, 13, 11, 18], [2]]

    for i in range(M):
        for j in range(len(T_info[i])):
            for k in range(j+1, len(T_info[i])):
                if T_info[i][j] < T_info[i][k]:
                    T_info[i][j], T_info[i][k] = T_info[i][k], T_info[i][j]

    # print(T_info)
    # [[13, 12, 11, 2], [2], [2], [18, 13, 12, 11, 2], [2], [2], [2], [2], [18, 13, 12, 11, 2], [2]]

    cnt = 0
    for i in range(M):
        for j in range(len(T_info[i])):
            # 해당 차량 가장 무거운 짐 받기
            a = T_info[i][0]
            cnt += a
            # 다른 차량에서 해당 짐 제거
            for k in range(M):
                for l in range(len(T_info[k])):
                    if T_info[k][l] == a:
                        T_info[k].pop(l)
                        break  # 해당 번호지워주고 다음트럭으로 이동하기 위해 브레이크
            break  # 한 짐을 받은 뒤에 그 차량에서 볼 일 없으니 브레이크

    print(f'#{tc} {cnt}')