import sys

sys.stdin = open('5177_binaryheap_input.txt')

for tc in range(1, T+1):
    N = int(input())
    info = list(map(int, input().split()))

    tree = [0] * (N+1)

    for i in range(N):
