import sys

sys.stdin = open('5432_쇠막대기자르기_input.txt')

T = int(input())

for tc in range(1, T + 1):
    stick = input()

    st_lst = []
    for a in stick:
        st_lst += a

    # 레이저 표현 전처리
    for i in range(len(st_lst)-1):
        if st_lst[i] + st_lst[i+1] == '()':
            st_lst[i] = 'r'
            st_lst[i+1] = 'a'

    # print(st_lst)
    # ['r', 'a', '(', '(', '(', 'r', 'a', 'r', 'a', ')', '(', 'r', 'a', ')', 'r', 'a', ')', ')', '(', 'r', 'a', ')']
    # ['(', '(', '(', 'r', 'a', '(', 'r', 'a', 'r', 'a', ')', ')', '(', 'r', 'a', ')', 'r', 'a', ')', ')', '(', 'r', 'a', 'r', 'a', ')']

    # 슬라이싱으로 계산
    total = 0  # 최종 stick 개수
    cnt = 0  # 레이저를 만날 때 생기는 스틱 개수
    tmp = 0  # 중간에 생기는 스틱에 대한 개수를 세기 위한 변수

    while len(st_lst) > 1:
        if st_lst[0] == '(':
            cnt += 1
            st_lst = st_lst[1:]
        elif st_lst[0] == ')':
            if st_lst[1] == '(':
                 tmp += 1
            cnt -= 1
            st_lst = st_lst[1:]
        elif st_lst[0] == 'r':
            total += (cnt + tmp)
            st_lst = st_lst[1:]
        else:
            st_lst = st_lst[1:]

    if st_lst[0] == 'a':
        total += 1
    else:
        total += cnt

    print(total)

    # total = 0
    # cnt = -1
    #
    # while len(stick) != 0:
    #     if stick[0] == '(':
    #         cnt += 1
    #         if stick[1] == ')':
    #             total += cnt
    #         stick = stick[1:]
    #     else:
    #         if len(stick) != 1 and stick[1] == '(':
    #             cnt = -1
    #         cnt -= 1
    #         stick = stick[1:]
    #
    #
    # print(f'#{tc} {total}')