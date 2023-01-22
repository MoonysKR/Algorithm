import sys

sys.stdin = open('input4.txt')

N, M = map(int, input().split())

lst_A = [[0] * M for _ in range(N)]
lst_B = [[0] * M for _ in range(N)]

for i in range(N):
    tmp = input()
    for j in range(M):
        if tmp[j] == '0':
            lst_A[i][j] = 0
        else:
            lst_A[i][j] = 1

for i in range(N):
    tmp = input()
    for j in range(M):
        if tmp[j] == '0':
            lst_B[i][j] = 0
        else:
            lst_B[i][j] = 1

cnt = 0

if N < 3 or M < 3:
    cnt = -1
elif lst_A == lst_B:
    pass
else:
    for i in range(N-2):
        for j in range(M-2):

            for k in range(3):
                for l in range(3):
                    if lst_A[i + k][j + l] == 0:
                        lst_A[i + k][j + l] = 1
                    else:
                        lst_A[i + k][j + l] = 0
            cnt += 1
            print('A', cnt)
            print(*lst_A, sep='\n')
            print('B', cnt)
            print(*lst_B, sep='\n')
            if lst_A == lst_B:
                break

        if lst_A == lst_B:
            break        

if lst_A != lst_B:
    cnt = -1

print(cnt)
