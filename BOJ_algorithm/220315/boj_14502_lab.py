import sys, copy

sys.stdin = open('boj_14502_lab_input.txt')


def infect(lst):
    lst_duplicate = copy.deepcopy(lst)
    for i in range(len(lst_duplicate)):
        for j in range(len(lst_duplicate[0])):
            if lst_duplicate[i][j] == 2:
                if i - 1 >= 0:
                    if lst_duplicate[i - 1][j] == 0:
                        lst_duplicate[i - 1][j] = 2
                if i + 1 <= len(lst_duplicate) - 1:
                    if lst_duplicate[i + 1][j] == 0:
                        lst_duplicate[i + 1][j] = 2
                if j - 1 >= 0:
                    if lst_duplicate[i][j - 1] == 0:
                        lst_duplicate[i][j - 1] = 2
                if j + 1 <= len(lst_duplicate[0]) - 1:
                    if lst_duplicate[i][j + 1] == 0:
                        lst_duplicate[i][j + 1] = 2
    if lst_duplicate != lst:
        return infect(lst_duplicate)
    else:
        num_virus = 0
        var_virus = []
        for i in range(N):
            for j in range(M):
                if lst_duplicate[i][j] == 2:
                    num_virus += 1
        var_virus += [num_virus]
        return var_virus


for tc in range(1, 4):
    N, M = list(map(int, input().split()))
    lab = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(lab)

    # [전략]
    # 3개의 벽 3을 세운 임의의 랩을 생성
    # 벽을 3이라 칭하고
    # 벽을 세웠던 위치를 담을 변수 [[[0, 0], [0, 0], [0, 0]]] * (0개수)C3
    # 0을 탐색하면서 위치를 담기
    # 2 주변의 0을 2로 바꾸면서 전파
    # 2 개수 세기
    # 또 담을 건데 탐색해서 벽을 담을 변수와 같은 값이 존재한다면 pass
    # 2를 이동시키면서 전파
    # 2개수 세기
    # 리스트에 담기
    # 최솟값 출력

    # 빈공간 empty 세기
    # empty = 0
    # for i in range(N):
    #     for j in range(M):
    #         if lab[i][j] == 0:
    #             empty += 1

    # loc_walls = [[[0, 0], [0, 0], [0, 0]]] * (empty * (empty-1) * (empty-2))
    loc_walls = []

    # lab의 복사본 생성
    lab_dup = copy.deepcopy(lab)

    walls = 0
    infect_nums = []
    for i in range(N):
        for j in range(M):
            if lab_dup[i][j] == 0:
                lab_dup[i][j] = 1
                for k in range(N):
                    for l in range(M):
                        if lab_dup[k][l] == 0:
                            lab_dup[k][l] = 1
                            for m in range(N):
                                for n in range(M):
                                    if lab_dup[m][n] == 0:
                                        lab_dup[m][n] = 1
                                        infect_nums += infect(lab_dup)
                                        lab_dup[m][n] = 0
                            lab_dup[k][l] = 0
                lab_dup[i][j] = 0

    min_num = infect_nums[0]
    for infect_num in infect_nums:
        if infect_num < min_num:
            min_num = infect_num

    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 1:
                cnt += 1

    safe = (N * M) - cnt - 3 - min_num

    print(safe)
