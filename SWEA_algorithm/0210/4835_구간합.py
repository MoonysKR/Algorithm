import sys

sys.stdin = open('4835_구간합.txt')

T = int(input())

for i in range(1, T+1):
    # N과 M으로 이루어진 list 생성 및 N, M 추출
    N_M_list = list(map(int, input().split()))
    N = N_M_list[0]
    M = N_M_list[1]

    # V list 추출
    V = list(map(int, input().split()))

    # 인접한 M개의 합을 담을 list
    total_list = []

    # 인접한 M개의 합 구해서 리스트에 담기

    # 인접한 M개의 수에서 뽑을 수 있는 마지막 index
    # e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 인접한 3개의 수의 마지막은 8, 9, 10 => 8의 인덱스는 10(N) - 3(M) = 7
    # range 함수에 넣을 때는 +1
    for k in range(0, N-M+1):
        total = 0  # total의 초기값
        # for p in range(k, k+M):
        start = k  # 시작 index
        end = M + k  # 마지막 index
        for p in range(start, end):  # e.g.에 따라 인접한 세 수가 도출되어
            total += V[p]           # total에 더해짐
        total_list += [total]       # total을 인자값으로 갖는 리스트

    # 최대합 최소합 구하기
    max_total = total_list[0]
    min_total = total_list[0]

    # total_list 인자값 호출
    for num in total_list:
        if num > max_total:
            max_total = num  # 최댓값
        if num < min_total:
            min_total = num  # 최솟값

    result = max_total - min_total  # 최댓값 - 최솟값

    print(f'#{i} {result}')



