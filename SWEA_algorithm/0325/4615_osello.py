import sys

sys.stdin = open('4615_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    seq = [list(map(int, input().split())) for _ in range(M)]
    # print(seq)
    # [[1, 2, 1], [1, 1, 2], [4, 3, 1], [4, 4, 2], [2, 1, 1], [4, 2, 2], [3, 4, 1], [1, 3, 2], [2, 4, 1], [1, 4, 2],
    #  [4, 1, 2], [3, 1, 2]]

    board = [[0]*N for _ in range(N)]
    board[len(board)//2][len(board)//2] = 2
    board[len(board)//2-1][len(board)//2] = 1
    board[len(board)//2][len(board)//2-1] = 1
    board[len(board)//2-1][len(board)//2-1] = 2
    # print(board)
    # [[0, 0, 0, 0],
    #  [0, 2, 1, 0],
    #  [0, 1, 2, 0],
    #  [0, 0, 0, 0]]

    for i in range(len(seq)):
        a = seq[i][1]-1  # y좌표
        b = seq[i][0]-1  # x좌표
        c = seq[i][2]  # 돌 색
        board[a][b] = c
        if b > 0:  # 좌
            for j in range(b-1, -1, -1):
                if board[a][j] == c:
                    for k in range(j+1, b):
                        board[a][k] = c
                    break
        if b < N-1:  # 우
            for j in range(b+1, N):
                if board[a][j] == c:
                    for k in range(b+1, j):
                        board[a][k] = c
                    break
        if a > 0:  # 상
            for j in range(a-1, -1, -1):
                if board[j][b] == c:
                    for k in range(j+1, a):
                        board[k][b] = c
                    break
        if a < N-1:  # 하
            for j in range(a+1, N):
                if board[j][b] == c:
                    for k in range(a+1, j):
                        board[k][b] = c
                    break
        if a > 0 and b > 0 :  #좌상
            if a < b:
                for j in range(a - 1, -1, -1):
                    if board[j][b-(a-j)] == c:
                        for k in range(j + 1, a):
                            board[k][b-(a-k)] = c
                        break
            else:
                for j in range(b - 1, -1, -1):
                    if board[a-(b-j)][j] == c:
                        for k in range(j + 1, b):
                            board[a-(b-k)][k] = c
                        break
        if a < N-1 and b < N-1:  # 우하
            if N - 1 - b < N - 1 - a:
                for j in range(b + 1, N):
                    if board[a-(b-j)][j] == c:
                        for k in range(b + 1, j):
                            board[a-(b-k)][k] = c
                        break
            else:
                for j in range(a + 1, N):
                    if board[j][b-(a-j)] == c:
                        for k in range(a + 1, j):
                            board[k][b-(a-k)] = c
                        break
        if 0 < a and b < N-1:  # 우상
            if a < N - 1 - b:
                for j in range(a - 1, -1, -1):
                    if board[j][b+(a-j)] == c:
                        for k in range(j + 1, a):
                            board[k][b+(a-k)] = c
                        break
            else:
                for j in range(b + 1, N):
                    if board[a+(b-j)][j] == c:
                        for k in range(b + 1, j):
                            board[a+(b-k)][k] = c
                        break
        if a < N - 1 and 0 < b:  # 좌하
            if N - 1 - a < b:
                for j in range(a + 1, N):
                    if board[j][b+(a-j)] == c:
                        for k in range(a + 1, j):
                            board[k][b+(a-k)] = c
                        break
            else:
                for j in range(b - 1, -1, -1):
                    if board[a+(b-j)][j] == c:
                        for k in range(j + 1, b):
                            board[a+(b-k)][k] = c
                        break

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')