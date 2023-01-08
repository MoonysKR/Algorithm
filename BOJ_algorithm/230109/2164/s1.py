import sys

sys.stdin = open('input1.txt')

from collections import deque

N = int(input())

cards = deque()

for i in range(1, N+1):
    cards.append(i)

while len(cards) != 1:
    cards.popleft()
    tmp_card = cards.popleft()
    cards.append(tmp_card)

print(cards[0])