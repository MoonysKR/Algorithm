import sys

sys.stdin = open('1231_input.txt')

def in_order(v):
    global info  # 글로벌에서 info 받아와주고
    global result  # 글로벌에서 결과를 추가해줄 result 받아와주고
    # 중위순회 시작
    if v != 0:
        in_order(ch1[v])
        result += info[v-1][1]  # 순서대로 저장
        in_order(ch2[v])


for tc in range(1, 11):
    V = int(input())
    info = [list(map(str, input().split())) for _ in range(V)]

    # print(info)
    # [['1', 'W', '2', '3'], ['2', 'F', '4', '5'], ['3', 'R', '6', '7'], ['4', 'O', '8'], ['5', 'T'], ['6', 'A'],
    #  ['7', 'E'], ['8', 'S']]

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)

    for i in range(V):
        if len(info[i]) == 4:
            ch1[int(info[i][0])] = int(info[i][2])
            ch2[int(info[i][0])] = int(info[i][3])
        if len(info[i]) == 3:
            ch1[int(info[i][0])] = int(info[i][2])

    # print(ch1, ch2)
    # [0, 2, 4, 6, 8, 0, 0, 0, 0][0, 3, 5, 7, 0, 0, 0, 0, 0]

    # 결과를 담아줄 빈 문자열
    result = ''

    # 노드 순서는 번호 순
    in_order(1)

    print(f'#{tc} {result}')