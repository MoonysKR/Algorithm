import sys

sys.stdin = open('5176_binary_tree_input.txt')

def tree(n):
    global num
    if n != 0:
        tree(ch1[n])  # 왼쪽 자식 노드 탐색
        nums[n] = num  # 부모 노드 값 입력
        num += 1  # 다음번호 저장
        tree(ch2[n])  # 오른쪽 자식 노드 탐색

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 부모 노드를 인덱스로 하는 자식 노드의 배열
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    if N % 2 == 0:
        for i in range(1, N//2+1):
            ch1[i] = 2 * i
        for i in range(1, N//2):
            ch2[i] = 2 * i + 1
    else:
        for i in range(1, N//2+1):
            ch1[i] = 2 * i
            ch2[i] = 2 * i + 1

    # print(ch1, ch2)
    # [0, 2, 4, 6, 0, 0, 0][0, 3, 5, 0, 0, 0, 0]

    # 노드를 인덱스로 담고 있는 값
    nums = [0] * (N+1)

    # 시작 값 설정
    num = 1

    # 값 넣어주기
    tree(1)

    print(f'#{tc} {nums[1]} {nums[N//2]}')

