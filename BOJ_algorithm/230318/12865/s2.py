import sys

sys.stdin = open('input1.txt')


def calculate(lst):
    global N, K, info

    weight = 0

    value = 0

    for i in range(N):
        if lst[i] == 1:
            weight += info[i][0]
            value += info[i][1]
            if weight > K:
                return 0, 0
    
    return weight, value

def check(num, weight):
    global N, K, max_value

    if weight > K:
        return

    if num == N - 1:
        weight, value = calculate(combination)
        if weight <= K and value > max_value:
            max_value = value

        combination[num] = 1
        weight, value = calculate(combination)
        if weight <= K and value > max_value:
            max_value = value
        combination[num] = 0

        return
    
    check(num + 1, weight + combination[num])
    combination[num] = 1
    check(num + 1, weight + combination[num])
    combination[num] = 0

N, K = map(int, input().split())

info = list(list(map(int, input().split())) for _ in range(N))

# print(info)
# [[6, 13], [4, 8], [3, 6], [5, 12]]

combination = [0] * N

max_value = 0

check(0, 0)

print(max_value)