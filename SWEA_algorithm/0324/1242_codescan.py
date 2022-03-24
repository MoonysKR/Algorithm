import sys

sys.stdin = open('1242_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    maps = [input() for _ in range(N)]
    # print(maps)
    # [['00000000000000000000000000'], ['00000000000000000000000000'], ['000000001DB176C588D26EC000'],
    #  ['000000001DB176C588D26EC000'], ['000000001DB176C588D26EC000'], ['000000001DB176C588D26EC000'],
    #  ['000000001DB176C588D26EC000'], ['000000001DB176C588D26EC000'], ['000000001DB176C588D26EC000'],
    #  ['000000001DB176C588D26EC000'], ['000000001DB176C588D26EC000'], ['000000001DB176C588D26EC000'],
    #  ['000000001DB176C588D26EC000'], ['000000001DB176C588D26EC000'], ['00000000000000000000000000'],
    #  ['00000000000000000000000000']]

    arr = [['0'] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if maps[i][j] != arr[i][j]:
                arr[i][j] = maps[i][j]
    # print(arr)

    codes = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                tmp = ''
                k = 0
                while arr[i][j+k] != '0':
                    tmp += arr[i][j+k]
                    arr[i][j+k] = '0'
                    k += 1
                if tmp not in codes and tmp != '':
                    codes += [tmp]

    # print(codes)
    # ['1DB176C588D26EC']
    # ['196EBC5A316C578', '328D1AF6E4C9BB']

    nums = []
    for i in range(len(codes)):
        num = []
        for j in range(len(codes[i])):
            num += [int(codes[i][j], 16)]
        nums += [num]

    # print(nums)
    # [[1, 13, 11, 1, 7, 6, 12, 5, 8, 8, 13, 2, 6, 14, 12]]
    # [[1, 9, 6, 14, 11, 12, 5, 10, 3, 1, 6, 12, 5, 7, 8], [3, 2, 8, 13, 1, 10, 15, 6, 14, 4, 12, 9, 11, 11]]

    fake_pwds = []
    for i in range(len(nums)):
        pwd = ''
        for j in range(len(nums[i])):
            tmp = ''
            for k in range(4):
                tmp = str(nums[i][j] % 2) + tmp
                nums[i][j] //= 2
            pwd += tmp
        fake_pwds += [pwd]

    # print(fake_pwds)
    # ['000111011011000101110110110001011000100011010010011011101100']
    # ['000110010110111010111100010110100011000101101100010101111000', '00110010100011010001101011110110111001001100100110111011']

    # 56의 배수개가 되도록 암호 코드 작업화
    for i in range(len(fake_pwds)):
        length = len(fake_pwds[i])
        while fake_pwds[i][-1] == '0':
            fake_pwds[i] = fake_pwds[i][:-1]
        while length // 56 * 56 < len(fake_pwds[i]):
            fake_pwds[i] = fake_pwds[i][1:]
        while length // 56 * 56 > len(fake_pwds[i]):
            fake_pwds[i] = '0' + fake_pwds[i]

    # print(fake_pwds)
    # ['01110110110001011101101100010110001000110100100110111011']
    # ['00110010110111010111100010110100011000101101100010101111', '00110010100011010001101011110110111001001100100110111011']

    tmp_pwds = []
    for fake_pwd in fake_pwds:
        tmp_pwd = []
        length = len(fake_pwd) // 56
        for i in range(8):
            tmp_pwd += [fake_pwd[:7*length]]
            fake_pwd = fake_pwd[7*length:]
        tmp_pwds += [tmp_pwd]

    # print(tmp_pwds)
    # [['0111011', '0110001', '0111011', '0110001', '0110001', '0001101', '0010011', '0111011']]
    # [['0011001', '0110111', '0101111', '0001011', '0100011', '0001011', '0110001', '0101111'], ['0011001', '0100011', '0100011', '0101111', '0110111', '0010011', '0010011', '0111011']]

    pwds = []
    for i in range(len(tmp_pwds)):
        pwd = ''
        length = len(fake_pwds[i]) // 56
        for j in range(len(tmp_pwds[i])):
            if tmp_pwds[i][j] == '000' * length + '11' * length + '0' * length + '1' * length:
                pwd += '0'
            elif tmp_pwds[i][j] == '00' * length + '11' * length + '00' * length + '1' * length:
                pwd += '1'
            elif tmp_pwds[i][j] == '00' * length + '1' * length + '00' * length + '11' * length:
                pwd += '2'
            elif tmp_pwds[i][j] == '0' * length + '1111' * length + '0' * length + '1' * length:
                pwd += '3'
            elif tmp_pwds[i][j] == '0' * length + '1' * length + '000' * length + '11' * length:
                pwd += '4'
            elif tmp_pwds[i][j] == '0' * length + '11' * length + '000' * length + '1' * length:
                pwd += '5'
            elif tmp_pwds[i][j] == '0' * length + '1' * length + '0' * length + '1111' * length:
                pwd += '6'
            elif tmp_pwds[i][j] == '0' * length + '111' * length + '0' * length + '11' * length:
                pwd += '7'
            elif tmp_pwds[i][j] == '0' * length + '11' * length + '0' * length + '111' * length:
                pwd += '8'
            elif tmp_pwds[i][j] == '000' * length + '1' * length + '0' * length + '11' * length:
                pwd += '9'
        pwds += [pwd]

    # print(pwds)
    # ['75755027']
    # ['18694956', '14468227']

    results = []
    for i in range(len(pwds)):
        even = 0
        odd = 0
        for j in range(len(pwds[i])):
            if j % 2 == 1:
                even += int(pwds[i][j])
            else:
                odd += int(pwds[i][j])
        if (3 * odd + even) % 10 == 0:
            results += [odd + even]
    # print(results)
    # [38]
    # [48]

    if len(results) == 0:
        results = [0]

    print(f'#{tc}', end=' ')
    print(*results)

