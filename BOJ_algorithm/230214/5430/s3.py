import sys

sys.stdin = open('input1.txt')

T = int(input())

for tc in range(T):
    
    funcs = input()

    n = int(input())

    tmp = input()

    tmp = tmp[1:-1]
    # 1,2,3,4

    if tmp != '':
        lst = list(map(int, tmp.split(',')))
    else:
        lst = []

    result = ''


    # 몇번 뒤집을지 정하는 변수
    flip = 0

    flag = 0

    while flag == 0:
        # 함수를 모두 실행했으면
        if funcs == '':
            flag = 1

        # 첫번째 함수가 뒤집기면
        elif funcs[0] == 'R':
            cnt = 0
            for func in funcs:
                if func != 'R':
                    break
                else:
                    cnt += 1
            funcs = funcs[cnt:]
            flip += cnt
        
        # 첫번째 함수가 삭제라면
        elif funcs[0] == 'D':
            if len(lst) == 0:
                result = 'error'
                flag = 1
            else:
                cnt = 0
                for func in funcs:
                    if func != 'D':
                        break
                    else:
                        cnt += 1
                if len(lst) < cnt:
                    result = 'error'
                    flag = 1
                else:
                    if flip % 2 == 0:
                        lst = lst[cnt:]
                    else:
                        lst = lst[:-cnt]

                    funcs = funcs[cnt:]

    # print(lst)

    if result != 'error':
        if flip % 2 == 1:
            result = []
            for i in range(len(lst)):
                result = [lst[i]] + result
        else:
            result = lst
    
    print(result)


        

