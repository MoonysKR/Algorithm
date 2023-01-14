import sys

sys.stdin = open('input1.txt')

# def get_length(lst):
#     global cnt
#     # print(lst)
#     if lst:
#         first = lst[0]
#         second = lst[1]
#         cnt += second[1] - first[1]
#         get_length(lst[2:])
#     else:
#         return

from collections import deque

N = int(input())

row = []
vertical = []

for i in range(N):
    x, y = map(int, input().split())
    row.append((x, y))
    vertical.append((y, x))

# print(sorted(row), sorted(vertical))

new_row = deque(sorted(row))
new_vertical = deque(sorted(vertical))

cnt = 0

# get_length(new_row)
# get_length(new_vertical)

while new_row:
    first = new_row.popleft()
    second = new_row.popleft()
    third = new_vertical.popleft()
    fourth = new_vertical.popleft()
    cnt += second[1] + fourth[1] - third[1] - first[1]

print(cnt)