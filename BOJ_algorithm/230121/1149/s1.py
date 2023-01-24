import sys

sys.stdin = open('input5.txt')

def min_rgb(lst, before, where):
    global N, info, min_cost

    if len(lst) == N:
        if sum(lst) < min_cost:
            min_cost = sum(lst)

    if len(lst) == 0:
        for i in range(3):
            lst.append(info[where][i])
            if i == 0:
                min_rgb(lst, 'R', where + 1)
            elif i == 1:
                min_rgb(lst, 'G', where + 1)
            elif i == 2:
                min_rgb(lst, 'B', where + 1)
            lst.pop()


    if len(lst) > 0 and len(lst) < N:
        if sum(lst) > min_cost:
            return

        elif before == 'R':
            lst.append(info[where][1])
            min_rgb(lst, 'G', where + 1)
            lst.pop()
            lst.append(info[where][2])
            min_rgb(lst, 'B', where + 1)
            lst.pop()

        elif before == 'G':
            lst.append(info[where][0])
            min_rgb(lst, 'R', where + 1)
            lst.pop()
            lst.append(info[where][2])
            min_rgb(lst, 'B', where + 1)
            lst.pop()

        else:
            lst.append(info[where][0])
            min_rgb(lst, 'R', where + 1)
            lst.pop()
            lst.append(info[where][1])
            min_rgb(lst, 'G', where + 1)
            lst.pop()

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

# print(*info, sep= '\n')
# [26, 40, 83]
# [49, 60, 57]
# [13, 89, 99]

min_cost = 0

for i in range(N):
    min_cost += sum(info[i])

min_rgb([], '', 0)

print(min_cost)