import sys

sys.stdin = open('연습문제1_문자열뒤집기_문자열비교_input.txt')

T = int(input())

for tc in range(1, T+1):
    wrd = input()

    # 1. 새로운 str에 저장
    new_wrd = ''
    for alp in wrd:
        new_wrd = alp + new_wrd

    print(f'#{tc} {new_wrd}')

    # 2. 슬라이싱 이용
    new_wrd_2 = wrd[::-1]

    print(f'#{tc} {new_wrd_2}')