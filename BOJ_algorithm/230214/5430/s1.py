import sys

sys.stdin = open('input1.txt')

from collections import deque

T = int(input())

for tc in range(T):
    
    funcs = input()

    n = int(input())

    tmp = input()

    tmp = tmp[1:-1]
    # 1,2,3,4

    if tmp != '':
        lst = deque(map(int, tmp.split(',')))
    else:
        lst = deque([])

    # print(lst)
    # deque([1, 2, 3, 4])
    # deque([42])
    # deque([1, 1, 2, 3, 5, 8])
    # deque([])

    result = ''

    for func in funcs:
        # print(lst)

        if func == 'R':
            new_lst = deque([])
            for i in range(len(lst)):
                num = lst.pop()
                new_lst.append(num)
            lst = new_lst

        else:
            if len(lst) == 0:
                result = 'error'
                break
            else:
                lst.popleft()

    if result != 'error':
        result = list(lst)
        
    print(result)