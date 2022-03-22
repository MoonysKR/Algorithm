import sys

sys.stdin = open('5178_sum_node_input.txt')

T = int(input())

# 후진 탐색
def post_order_sum(L):
    total = 0  # 노드까지의 합을 더해줄 변수
    if L != 0:  # 없는 노드가 아니라면
        post_order_sum(ch1[L])  # 왼쪽으로 한 번 더 내려가보기
        post_order_sum(ch2[L])  # 오른쪽으로 한 번 더 내려가보기
        # 부모 노드를 처리해줄건데
        if tree_num[ch1[L]] != 0:  # 왼쪽 자식 노드의 값이 0 이 아니라면...(없는 것이 아니라면)  // 사실 없는게 아니라 0번째 값으로 가서 0이됨.
            total += tree_num[ch1[L]]  # 노드까지의 합에 추가해주고
            tree_num[L] = tree_num[L] + tree_num[ch1[L]]  # 부모 노드의 값을 변경해주기
        if tree_num[ch2[L]] != 0:
            total += tree_num[ch2[L]]
            tree_num[L] = tree_num[L] + tree_num[ch2[L]]
    return total

for tc in range(1, T+1):
    # N = 노드 개수
    # M = 리프 노드의 개수
    # L = 값을 출력할 노드 번호

    N, M, L = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(M)]

    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    if N % 2 == 1:
        for i in range(1, N//2+1):
            ch1[i] = 2 * i
            ch2[i] = 2 * i + 1
    else:
        for i in range(1, N//2+1):
            ch1[i] = 2 * i
        for j in range(1, N//2):
            ch2[j] = 2 * j + 1

    # print(ch1, ch2)
    # [0, 2, 4, 0, 0, 0][0, 3, 5, 0, 0, 0]

    # 값이 저장되어 있는 리스트
    tree_num = [0] * (N+1)
    for data in info:
        tree_num[data[0]] = data[1]

    # print(tree_num)
    # [0, 0, 0, 3, 1, 2]

    print(f'#{tc} {post_order_sum(L)}')