import sys

sys.stdin = open('input1.txt')

from collections import deque

N = int(input())

points = []

for i in range(N):
    x, y = map(int, input().split())
    points.append((y, x))

print(points.sort)


