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
        lst = deque(list(map(int, tmp.split(','))))
    else:
        lst = deque([])

    flip = 0

    result = ''

    for func in funcs:

        # 좌우회전이라면
        if func == 'R':
            flip += 1
        
        # 지우기라면
        elif func == 'D':
            # 지울게 없으면 에러
            if len(lst) == 0:
                result = 'error'
                break
            else:
                # 홀수 번 뒤집을거라면 우측 팝
                if flip % 2 == 1:
                    lst.pop()
                # 짝수 번 뒤집을거라면 좌측 팝
                else:
                    lst.popleft()

    if result == 'error':
        print('error')

    else:
        if flip % 2 == 1:
            lst.reverse()
            result = '['
            for num in lst:
                result += str(num)
                result += ','
            if result != '[':
                result = result[:-1]
            result += ']'
            
        else:
            result = '['
            for num in lst:
                result += str(num)
                result += ','
            if result != '[':
                result = result[:-1]
            result += ']'
        print(result)