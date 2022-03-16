import sys

sys.stdin = open('1216_회문2_input.txt')

for _ in range(1, 11):
    tc = input()
    snts = [input() for _ in range(100)]

    # 회문 길이와 횟수를 담을 리스트
    cnt_lst = []

    # 행 탐색
    for i in range(1, 101):
        len_pal = i  # 길이가 i인 회문 탐색
        cnt = 0  # 회문 발견 횟수
        pal_str = ''  # 회문인지 판단할 문자열
        for j in range(100):
            for k in range(101-i):  # 시작점
                for l in range(i//2):  # 앞 i//2개만 탐색
                    if snts[j][k+l] == snts[j][k+i-l-1]:
                        pal_str += snts[j][k+l]
                if len(pal_str) == i//2:  # 회문 찾음
                    cnt += 1  # 회문 발견 횟수 증가
                    pal_str = ''  # 리셋
                else:  # 회문 못찾음
                    pal_str = ''  # 리셋
        cnt_lst += [cnt]

    # 열 탐색
    for i in range(1, 101):
        len_pal = i
        cnt = 0
        pal_str = ''
        for j in range(100):
            for k in range(101-i):
                for l in range(i//2):
                    if snts[k+l][j] == snts[k+i-l-1][j]:
                        pal_str += snts[k+l][j]
                if len(pal_str) == i//2:
                    cnt += 1
                    pal_str = ''
                else:
                    pal_str = ''
        cnt_lst[i-1] += cnt

    # 회문 횟수가 담긴 리스트의 0이 아닌 마지막 숫자의 인덱스값이 회문의 길이
    for m in range(100):
        if cnt_lst[m] != 0:
            max_cnt = m + 1

    print(f'#{tc} {max_cnt}')
