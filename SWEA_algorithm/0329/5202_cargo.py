import sys

sys.stdin = open('5202_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    reservations = [list(map(int, input().split())) for _ in range(N)]
    # print(trucks)
    # [[20, 23], [17, 20], [23, 24], [4, 14], [8, 18]]

    # 트럭번호와 소요시간 정리
    trucks_info = []
    for i in range(N):
        trucks_info += [[i, reservations[i][1] - reservations[i][0]]]
    # print(trucks_info)
    # [[0, 3], [1, 3], [2, 1], [3, 10], [4, 10]]

    # 시간이 덜 걸리는 순서로 정렬
    for i in range(N):
        for j in range(i, N):
            if trucks_info[i][1] > trucks_info[j][1]:
                trucks_info[i], trucks_info[j] = trucks_info[j], trucks_info[i]
    # print(trucks_info)
    # [[2, 1], [1, 3], [0, 3], [3, 10], [4, 10]]


    # 시간이 덜 걸리는 순서대로 시간표 확인하고 채워주는 작업
    table = [0] * 24
    # 발주 건수
    cnt = 0
    for i in range(N):
        a = trucks_info[i][0]  # 인덱스가 길어지기때문에 임시로 설정
        if 1 not in table[reservations[a][0]:reservations[a][1]]:  # 시간표에 예약된게 없으면
            for j in range(reservations[a][0], reservations[a][1]):  # 채워주기
                table[j] = 1
            cnt += 1  # 발주 건수 추가


    print(f'#{tc} {cnt}')



