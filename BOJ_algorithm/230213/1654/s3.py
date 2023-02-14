import sys

sys.stdin = open('input1.txt')

N, K = map(int, input().split())

lines = []

for _ in range(N):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    cnt = 0 #랜선 수
    for i in lines:
        cnt += i // mid #분할 된 랜선 수
        
    if cnt >= K: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1

print(end)