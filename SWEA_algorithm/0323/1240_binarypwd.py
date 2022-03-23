import sys

sys.stdin = open('1240_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]

    # 모든 암호는 1로 끝난다.
    # 뒤부터 순회 했을 때 1이 끝나는 지점
    tmp = []
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                tmp += [i, j]
                break
    # print(tmp)
    # [12, 69, 11, 69, 10, 69, 9, 69, 8, 69, 7, 69, 6, 69]

    codes = arr[tmp[0]][tmp[1]-55:tmp[1]+1]
    # print(codes)
    # 01110110110001011101101100010110001000110100100110111011

    tmp_codes = []
    for i in range(8):
        tmp_codes += [codes[:7]]
        codes = codes[7:]

    # print(tmp_codes)
    # ['0111011', '0110001', '0111011', '0110001', '0110001', '0001101', '0010011', '0111011']

    pwd = ''
    for i in range(len(tmp_codes)):
        if tmp_codes[i] == '0001101':
            pwd += '0'
        elif tmp_codes[i] == '0011001':
            pwd += '1'
        elif tmp_codes[i] == '0010011':
            pwd += '2'
        elif tmp_codes[i] == '0111101':
            pwd += '3'
        elif tmp_codes[i] == '0100011':
            pwd += '4'
        elif tmp_codes[i] == '0110001':
            pwd += '5'
        elif tmp_codes[i] == '0101111':
            pwd += '6'
        elif tmp_codes[i] == '0111011':
            pwd += '7'
        elif tmp_codes[i] == '0110111':
            pwd += '8'
        elif tmp_codes[i] == '0001011':
            pwd += '9'

    # print(pwd)
    # 75755027

    result = 0
    for i in range(8):
        if (i+1) % 2 == 1:
            result += int(pwd[i]) * 3
        else:
            result += int(pwd[i])

    final = 0
    for num in pwd:
        final += int(num)

    if result % 10 == 0:
        print(f'#{tc} {final}')
    else:
        print(f'#{tc} 0')