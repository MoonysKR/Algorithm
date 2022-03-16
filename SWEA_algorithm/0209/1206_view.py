import sys

sys.stdin = open('input_1206_view.txt')

for tc in range(1, 11):

    T = int(input())

    # 빌딩 정보 불러오기
    buildings = list(map(int, input().split()))

    # 조망 값을 담을 리스트
    views =[]

    for r in range(2, T-2):
        # 최솟값 구하기 // 리스트 값에 차이 넣고 최솟값 확인
        vw = []
        vw_1 = [buildings[r] - buildings[r-2]]
        vw_2 = [buildings[r] - buildings[r-1]]
        vw_3 = [buildings[r] - buildings[r+1]]
        vw_4 = [buildings[r] - buildings[r+2]]
        vw = vw_1 + vw_2 + vw_3 + vw_4

        # list에서 최솟값 추출
        vw_point = vw[0]
        for i in range(4):
            if vw[i] < vw_point:
                vw_point = vw[i]
        views += [vw_point]

    # 전망 점수가 0 이상인 값들의 합
    total_view = 0
    for view in views:
        if view > 0:
            total_view += view

    print(f'#{tc} {total_view}')





