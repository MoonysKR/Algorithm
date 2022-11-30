

import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

info = [[] for _ in range(N)]

# print(lst)

for i in range(M):
    j, k = map(int, input().split())
    info[j-1] += [k-1]
    info[k-1] += [j-1]

lst = [[0] * N for _ in range(N)]

# print(info)

# print(lst)

# kevin_baicon = [0] * N

max_len = 0
which = 0

for i in range(len(info)):
    if len(info[i]) > max_len:
        max_len = len(info[i])
        which = i+1

print(which)

# for i in range(N):
#     min_cnt = (N-1) * (N-1)
#     for j in range(i, N):
#         if i == j:
#             pass
#         else:
#             cnt = 1
#             loc = i
#             while loc != j:
#                 for k in range(len(info[loc])):
#                     loc = info[loc][k]

# def find(start, )

            
                

