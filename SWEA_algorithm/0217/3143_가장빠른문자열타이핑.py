import sys

sys.stdin = open('3143_가장빠른문자열타이핑_input.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = list(map(str, input().split()))

    # banananananana
    # bana

    # 타이핑 + 단축키 사용횟수
    cnt = 0

    # A의 앞부분을 슬라이싱으로 잘라줄 예정
    # A가 B보다 짧아지면 종료
    while len(A) >= len(B):
        tmp = ''
        for i in range(len(B)):
            if A[i] == B[i]:
                tmp += A[i]
        if tmp == B:  # B랑 일치했기 때문에
            A = A[len(B):]  # B의 길이만큼 슬라이싱
            cnt += 1  # 단축키 사용횟수 추가
        else:  # B랑 달랐기 때문에
            A = A[1:]  # 한글자 슬라이싱
            cnt += 1  # 타이핑 횟수 추가
    result = cnt + len(A)  # (단축키+타이핑) + 나머지 글자

    print(f'#{tc} {result}')





