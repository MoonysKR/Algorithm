import sys

sys.stdin = open('1213_String_input.txt', encoding='utf-8')

for _ in range(1, 11):
    tc = int(input())
    wrd = input()  # 세어질 문자열
    snt = input()  # 비교할 문자열

    # brute_force
    cnt = 0
    for i in range(len(snt)-len(wrd)+1):  # index값 초과하지 않게 조심, 끝부분 맞추기
        tmp = ''  # 빈문자열 => 하나씩 채워서 비교할 예정
        for j in range(len(wrd)):
            tmp += snt[i+j]  # 빈 문자열에 하나씩 그냥 추가
        if tmp == wrd:  # 다 넣었을 때 같다면 cnt 1씩 증가
            cnt += 1

    print(f'#{tc} {cnt}')

    # KMP
    M = len(wrd)
    N = len(snt)
    lps = [0] * (M+1)
    j = 0
    for i in range(1, M):
        lps[i] = j
        if wrd[i]


    # 개수 초기화 값
    # cnt = 0
    # for i in range(len(snt)-len(wrd)+1):  # index값 초과하지 않게 조심, 끝부분 맞추기
    #     tmp = ''  # 빈문자열 => 하나씩 채워서 비교할 예정
    #     for j in range(len(wrd)):  # 앞에가 맞으면 다음으로 넘어갈 예정
    #         if wrd[j] == snt[i+j]:
    #             tmp += wrd[j]
    #     if tmp == wrd:  # 다 넣었을 때 같다면 cnt 1씩 증가
    #         cnt += 1
    #
    # print(f'#{tc} {cnt}')

    lps = [0] * (M+)
    j = 0
