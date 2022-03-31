import sys

sys.stdin = open('5208_input.txt')


def bus(start):
    global Ms, N, cnt
    # print(f'{tc} {start}')
    if start + Ms[start] < N:  # 시작점이 종착점 인덱스보다 작을 때
        mx = 0  # 최대로 갈 수 있는 인덱스 담아줄 예정
        ml = 0  # 최대로 갈 수 있는 길이를 담아줄 예정
        for i in range(start + 1, start + Ms[start] + 1):  # 시작점을 기준으로 갈 수 있는 위치의 인덱스까지 순회
            if i + Ms[i] >= N:  # 해당 인덱스에서 갈 수 있는 거리가 종착역보다 크거나 같을 때
                cnt += 1  # 횟수 추가
                # print(f'{tc} {i}')
                return cnt  # 종료
            elif i + Ms[i] > ml:  # 해당 인덱스에서 갈 수 있는 최대거리 구해주고 인덱스를 mx에 담아주기
                ml = i + Ms[i]
                mx = i
        # print(f'{tc} mx', mx)
        cnt += 1  # 담았으면 횟수 추가
        return bus(mx)  # 해당 인덱스를 시작점으로 다시 함수 호출
    else:  # 시작점이 종착점 인덱스보다 크거나, 스타트에서 이동가능한 거리가 종착역보다 클 때(중간에 들릴 필요 없음)
        return cnt


T = int(input())

for tc in range(1, T + 1):
    info = list(map(int, input().split()))
    N = info[0]
    Ms = [0] + info[1:]
    # print(Ms)
    # [0, 2, 3, 1, 1]

    # 시작점
    start = 1
    # 충전횟수
    cnt = 0

    print(f'#{tc} {bus(start)}')
