import sys

sys.stdin = open('input9.txt')

N = int(input())

infos = input()
switches = []

for info in infos:
    if info != ' ':
        switches += [int(info)]

# print(switches)
# [0, 1, 0, 1, 0, 0, 0, 1]

std_num = int(input())

for _ in range(std_num):
    sex, num = map(int, input().split())
    # print(sex, num)
    # 1 3
    # 2 3

    # 남학생이면
    if sex == 1:
        # 배수 개수만큼
        togo = len(switches) // num
        for j in range(1, togo + 1):
            if switches[num * j - 1] == 0:
                switches[num * j - 1] = 1
            else:
                switches[num * j - 1] = 0
    
        # print(switches)
        # [0, 1, 1, 1, 0, 1, 0, 1]

    # 여학생이면
    else:
        flag = 0
        cnt = 0
        while flag == 0:
            if num - 1 - cnt >= 0 and num - 1 + cnt < N:
                if switches[num - 1 - cnt] == switches[num - 1 + cnt]:
                    if switches[num - 1 - cnt] == 0:
                        switches[num - 1 - cnt] = 1
                        switches[num - 1 + cnt] = 1
                    else:
                        switches[num - 1 - cnt] = 0
                        switches[num - 1 + cnt] = 0
                    cnt += 1
                else:
                    flag = 1
            else:
                flag = 1


# rows = (N - 1) // 20

# for i in range(rows + 1):
#     if i == rows:
#         print(*switches[20 * i : (20 * i) + (N % 20)])
#         # 20을 20으로 나눈 나머지는 없음
#     else:
#         print(*switches[20 * i : (20 * i) + 20])

for i in range(0, N, 20): 
    print(*switches[i:i+20])