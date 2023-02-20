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

    flag = 0

    while flag == 0:

        if funcs == '':
            flag = 1

        elif funcs[0] == 'R':
            if len(lst) == 0:
                cnt = 0
                for func in funcs:
                    if func != 'R':
                        break
                    else:
                        cnt += 1
                funcs = funcs[cnt:]
            else:
                cnt = 0
                for func in funcs:
                    if func != 'R':
                        break
                    else:
                        cnt += 1
                if cnt % 2 == 1:
                    # lst.reverse()
                    new_lst = []
                    for i in range(len(lst)):
                        new_lst = [lst[i]] + new_lst
                    lst = new_lst
                funcs = funcs[cnt:]

        
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
                    lst = lst[cnt:]
                    funcs = funcs[cnt:]

    if result != 'error':
        result = lst
        
    print(result)