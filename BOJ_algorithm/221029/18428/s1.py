def get_max(count, info):

    global N, flag, teachers, block_history
    # print(block_history)                       
    
    if count == 3:
        for teacher in teachers:
            loc_y, loc_x = teacher
            # 상
            if loc_y > 0:
                for i in range(loc_y - 1, -1, -1):
                    if info[i][loc_x] == 'S':
                        blocks = []
                        for i in range(N):
                            for j in range(N):
                                if info[i][j] == 'B':
                                    blocks += [(i, j)]
                        block_history += [sorted(blocks)]
                        return
                    elif info[i][loc_x] == 'B':
                        break
                    else: # X , T
                        pass
            # 하
            if loc_y < N-1:
                for i in range(loc_y + 1, N):
                    if info[i][loc_x] == 'S':
                        blocks = []
                        for i in range(N):
                            for j in range(N):
                                if info[i][j] == 'B':
                                    blocks += [(i, j)]
                        block_history += [sorted(blocks)]                          
                        return
                    elif info[i][loc_x] == 'B':
                        break
                    else:
                        pass
            # 좌
            if loc_x > 0:
                for i in range(loc_x - 1, -1, -1):
                    if info[loc_y][i] == 'S':
                        blocks = []
                        for i in range(N):
                            for j in range(N):
                                if info[i][j] == 'B':
                                    blocks += [(i, j)]
                        block_history += [sorted(blocks)]                          
                        return
                    elif info[loc_y][i] == 'B':
                        break
                    else:
                        pass    
            # 우
            if loc_x > 0:
                for i in range(loc_x + 1, N):
                    if info[loc_y][i] == 'S':
                        blocks = []
                        for i in range(N):
                            for j in range(N):
                                if info[i][j] == 'B':
                                    blocks += [(i, j)]
                        block_history += [sorted(blocks)]                        
                        return
                    elif info[loc_y][i] == 'B':
                        break
                    else:
                        pass
        flag = 1
        return          

    elif count == 2:
        for i in range(N):
            for j in range(N):
                if info[i][j] == 'X':

                    info[i][j] = 'B'

                    blocks = []
                    for k in range(N):
                        for l in range(N):
                            if info[k][l] == 'B':
                                blocks += [(k, l)]
                    if sorted(blocks) in block_history:
                        return
                    
                    get_max(count+1, info)

    else:
        for i in range(N):
            for j in range(N):
                if info[i][j] == 'X':
                    info[i][j] = 'B'
                    get_max(count+1, info)



import sys

sys.stdin = open('input2.txt')

N = int(input())

info = [list(input().split()) for i in range(N)]

# print(info)

teachers = []

for i in range(N):
    for j in range(N):
        if info[i][j] == 'T':
            teachers += [(i, j)]

count = 0

block_history = []

flag = 0

get_max(count, info)

if flag == 1:
    print('YES')
else:
    print('NO')

