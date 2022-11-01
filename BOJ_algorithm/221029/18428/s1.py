def get_max(count, info):

    global N, flag, teachers, block_history
    # print(block_history)                       
    
    if count == 3:
        
        blocks = []
        for k in range(N):
            for l in range(N):
                if info[k][l] == 'B':
                    blocks += [(k, l)]
        if sorted(blocks) in block_history:
            return

        for teacher in teachers:
            loc_y, loc_x = teacher
            # 상
            if loc_y > 0:
                for i in range(loc_y - 1, -1, -1):
                    if info[i][loc_x] == 'S':  # 학생이 보인다면 장애물 히스토리에 리스트 추가해주고 리턴
                        blocks = []
                        for i in range(N):
                            for j in range(N):
                                if info[i][j] == 'B':
                                    blocks += [(i, j)]
                        block_history += [sorted(blocks)]
                        return
                    elif info[i][loc_x] == 'B':  # 장애물이 보인다면 더 볼 필요 없이 for문 종료
                        break
                    else: # X , T 이면 지나가자
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
            if loc_x < N-1:
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
        print(info)
        flag = 1
        return          

    elif count == 2:
        for i in range(N):
            for j in range(N):
                if info[i][j] == 'X':

                    info[i][j] = 'B'
                    
                    get_max(count+1, info)
                    info[i][j] = 'X'

    else :
        for i in range(N):
            for j in range(N):
                if info[i][j] == 'X':
                    info[i][j] = 'B'
                    get_max(count+1, info)
                    info[i][j] = 'X'



import sys

sys.stdin = open('input4.txt')

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