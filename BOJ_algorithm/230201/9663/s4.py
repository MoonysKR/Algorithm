import sys

sys.stdin = open('input1.txt')

def get_queens(lst1, lst2, lst3, idx):
    global N, cnt
    
    if idx == N:
        cnt += 1
        return

    for i in range(N):
        if lst1[i] == 0 and lst2[N - 1 - idx + i] == 0 and lst3[2 * N - 2 - idx - i] == 0:
            lst1[i] = 1
            lst2[N - 1 - idx + i] = 1
            lst3[2 * N - 2 - idx - i] = 1
            get_queens(lst1, lst2, lst3, idx + 1)
            lst1[i] = 0
            lst2[N - 1 - idx + i] = 0
            lst3[2 * N - 2 - idx - i] = 0




N = int(input())

cnt = 0

# 세로줄 인덱스
lst1 = [0 for _ in range(N)]
# 좌상단 - 우하단 인덱스
lst2 = [0 for _ in range(2 * N - 1)]
# 우상단 - 좌하단 인덱스
lst3 = [0 for _ in range(2 * N - 1)]


get_queens(lst1, lst2, lst3, 0)

print(cnt)

# for i in range(1, 16):
#     N = i
    
#     cnt = 0

#     # 세로줄 인덱스
#     lst1 = [0 for _ in range(N)]
#     # 좌상단 - 우하단 인덱스
#     lst2 = [0 for _ in range(2 * N - 1)]
#     # 우상단 - 좌하단 인덱스
#     lst3 = [0 for _ in range(2 * N - 1)]


#     get_queens(lst1, lst2, lst3, 0)

#     print(i, cnt)