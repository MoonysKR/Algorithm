import sys

sys.stdin = open('practice3_input.txt')

def pre_order(n):
    print(n, end=' ')
    if ch1[n] != 0:
        pre_order(ch1[n])
    if ch2[n] != 0:
        pre_order(ch2[n])

def in_order(n):
    if ch1[n] != 0:
        in_order(ch1[n])
    print(n, end=' ')
    if ch2[n] != 0:
        in_order(ch2[n])

def back_order(n):
    if ch1[n] != 0:
        in_order(ch1[n])
    if ch2[n] != 0:
        in_order(ch2[n])
    print(n, end=' ')


V = int(input())
infos = list(map(int, input().split()))
# print(infos)

ch1 = [0] * (V+2)
ch2 = [0] * (V+2)

for i in range(0, len(infos), 2):
    if ch1[infos[i]] == 0:
        ch1[infos[i]] = infos[i+1]
    else:
        ch2[infos[i]] = infos[i+1]

# print(ch1, ch2)
# [0, 2, 4, 5, 7, 8, 10, 12, 0, 0, 0, 13, 0] [0, 3, 0, 6, 0, 9, 11, 0, 0, 0, 0, 0, 0]

pre_order(1)
print()
in_order(1)
print()
back_order(1)
