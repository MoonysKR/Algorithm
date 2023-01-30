import sys

sys.stdin = open('input3.txt')

N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

# print(*maps, sep='\n')
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]

def get_ways(y, x, direction):
    global N, maps, cnt

    if y == N - 1 and x == N - 1:
        cnt += 1

    # 수평으로 들어올 때
    elif direction == 0:
        # 값 채워주기

        # 수평으로 내보내기
        # 가야할 다음 곳이 벽과 장애물이 아닐 경우
        
        if x <= N - 2:
            if maps[y][x + 1] != 1:
                get_ways(y, x + 1, 0)
        
        # 사선으로 보내기
        # 가야할 y, x가 N - 1 보다 작고, 길목에 방해물이 없을 경우
        if x <= N - 2 and y <= N - 2 and maps[y][x + 1] != 1 and maps[y + 1][x] != 1 and maps[y + 1][x + 1] != 1:
            # 사선으로 보내기
            get_ways(y + 1, x + 1, 1)

    # 수직으로 들어올 때
    elif direction == 2:
        # 값 채워주기
        

        # 수직으로 보내기     
        # 가야할 다음 곳이 벽과 장애물이 아닐 경우
        if y <= N - 2:
            if maps[y + 1][x] != 1:    
                get_ways(y + 1, x, 2)

        # 사선으로 보내기
        # 가야할 y, x가 N - 1 보다 작고, 길목에 방해물이 없을 경우
        if x <= N - 2 and y <= N - 2 and maps[y][x + 1] != 1 and maps[y + 1][x] != 1 and maps[y + 1][x + 1] != 1:
            # 사선으로 보내기
            get_ways(y + 1, x + 1, 1)
            
    # 사선으로 들어올 때
    else:
        # 값 채워주기
        # 수평으로 내보내기
        # 가야할 다음 곳이 벽과 장애물이 아닐 경우
        if x <= N - 2:
            if maps[y][x + 1] != 1:
                get_ways(y, x + 1, 0)
        
        # 수직으로 보내기
        # 가야할 다음 곳이 벽과 장애물이 아닐 경우
        if y <= N - 2:
            if maps[y + 1][x] != 1:    
                get_ways(y + 1, x, 2)

        # 사선으로 보내기
        # 가야할 y, x가 N - 1 보다 작고, 길목에 방해물이 없을 경우
        if x <= N - 2 and y <= N - 2 and maps[y][x + 1] != 1 and maps[y + 1][x] != 1 and maps[y + 1][x + 1] != 1:
            # 사선으로 보내기
            get_ways(y + 1, x + 1, 1)



get_ways(0, 1, 0)
        
print(cnt)