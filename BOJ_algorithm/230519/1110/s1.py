# import sys

# sys.stdin = open('input1.txt')

# N = int(input())

# cycle = 1

# first = N // 10

# second = N % 10

# previous = first + second

# new_number = 0

# while N != new_number:
#     if cycle == 1:
#         new_number = first * 10 + previous
#         cycle += 1
#     else:
#         if cycle != 4:
#             previous = new_number
#             new_number = (tmp % 10) * 10 + new_number % 10
#             cycle += 1
#             print(tmp, previous, new_number)
#         else:
#             break

# print(cycle)