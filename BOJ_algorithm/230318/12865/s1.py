import sys

sys.stdin = open('input1.txt')

def get(stuff, weight, value):
    global N, K, info, max_value

    # print(stuff, weight, value)

    if weight > K:
        return

    if value > max_value:
        max_value = value
    
    if stuff != N - 1:
        for i in range(stuff + 1, N):
            if info[i][0] + weight <= K:
                get(i, info[i][0] + weight, info[i][1] + value)

N, K = map(int, input().split())

info = list(list(map(int, input().split())) for _ in range(N))

# print(info)
# [[6, 13], [4, 8], [3, 6], [5, 12]]

max_value = 0

for i in range(N):
    get(i, info[i][0], info[i][1])

print(max_value)