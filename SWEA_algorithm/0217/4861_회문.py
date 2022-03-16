import sys

sys.stdin = open('4861_회문_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # print(N)
    snt = [input() for _ in range(N)]
    # print(snt)

    # 가로 방향 회문 찾기
    # 문장 불러오기, 처음부터 비교, 끝부분 인덱스 맞추기

    for i in range(N):
        for j in range(N-M+1):  # 문장 하나의 단어개수 고려
            result = ''
            for k in range(M//2):  # 선택된 단어의 앞부분 M//2개만 불러와 뒤에와 비교
                if snt[i][j+k] == snt[i][j+M-k-1]:
                    result += snt[i][j+k]  # 같다면 앞부분만 담아주기
            if len(result) == M // 2:  # result의 길이와 M//2의 길이가 같다면 찾음을 의미, 뒷부분 채워주기
                if M % 2 == 0:  # 짝수일 경우에는 result 값에서 호출하여 추가
                    for l in range(M//2):
                        result += result[M//2-l-1]
                    print(f'#{tc} {result}')
                else:  # 홀수일 경우에는 선택된 단어에서 중간 단어 추가 후 result 값에서 호출하여 추가
                    result += snt[i][M//2]
                    for l in range(M // 2):
                        result += result[M//2-l-1]
                    print(f'#{tc} {result}')

    # 세로 방향 회문 찾기
    for i in range(N):
        for j in range(N-M+1):
            result = ''
            for k in range(M//2):
                if snt[j+k][i] == snt[j+M-k-1][i]:
                    result += snt[j+k][i]
            if len(result) == M // 2:
                if M % 2 == 0:
                    for l in range(M // 2):
                        result += result[M // 2 - l - 1]
                    print(f'#{tc} {result}')

                else:
                    result += snt[M//2][i]
                    for l in range(M // 2):
                        result += result[M // 2 - l - 1]
                    print(f'#{tc} {result}')



