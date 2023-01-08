import sys

sys.stdin = open('input1.txt')

N = int(input())

records = {}

for i in range(N):
    book = input()
    if book in records.keys():
        records[book] += 1
    else:
        records[book] = 1

best_seller = 0


for i in range(len(records.values())):
    if records.values()[i] > best_seller:
        best_seller = records.values()[i]

print(best_seller)

print(records)