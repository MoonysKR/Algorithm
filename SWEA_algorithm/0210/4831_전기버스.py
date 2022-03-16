import sys

sys.stdin = open('4831_전기버스.txt')

T = int(input())

for tc in range(1, T+1):
    K_N_M = list(map(int, input().split()))
    K = K_N_M[0]  # 버스 이동 횟수
    N = K_N_M[1]  # 정류장 수
    M = K_N_M[2]  # 충전기 수
    M_locations = list(map(int, input().split()))  # 충전기 위치
    # [1 ,3 ,5, 7, 9]
    # [1, 3, 7, 8, 9]

    # 정류장과 충전기 리스트
    stations = [0] * (N+1)
    for M_location in M_locations:
        stations[M_location] = M_location
    # [0, 1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
    # [0, 1, 0, 3, 0, 0, 0, 7, 8, 9, 0]
    # [0, 0, 0, 0, 4, 0, 0, 7, 0, 9, 0, 0, 0, 0, 14, 0, 0, 17, 0, 0, 0]


    bus_fuel = K + 1
    for st_num in range(N+1):
        bus_fuel -= 1
        charges = 0
        if bus_fuel < 0:
            print(f'#{tc} 0')
        if st_num == stations[st_num]:
            for n in range(st_num+1, st_num+K+1):
                if stations[n] == True:
                    bus_fuel = bus_fuel
                else:
                    bus_fuel = K
                    charges += 1
    print(f'#{tc} {charges}')


