import sys

sys.stdin = open('4834_숫자카드.txt')

T = int(input())

for i in range(1, T+1):
    N = int(input())

    # 숫자 받아와 리스트 생성
    nums = list(map(int, input()))

    # 0~9 숫자 인덱스를 가지고 횟수를 담을 리스트 생성
    num_cnt_list = [0] * 10

    # nums list에 있는 횟수 num_list에 추가
    for num in nums:
        num_cnt_list[num] += 1

    # 가장 많이 등장한 횟수 도출
    cnt = num_cnt_list[0]
    for num_cnt in num_cnt_list:
        if num_cnt > cnt:
            cnt = num_cnt

    # 가장 많이 등장한 숫자 도출 (0부터 시작하기에 중복되는 경우 큰수로 대체됨)
    what_num = 0
    for k in range(0,10):
        if num_cnt_list[k] == cnt:
            what_num = k

    print(f'#{i} {what_num} {cnt}')