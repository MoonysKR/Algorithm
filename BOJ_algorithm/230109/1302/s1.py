import sys

sys.stdin = open('input5.txt')

N = int(input())

records = {}

for i in range(N):
    book = input()
    if book in records.keys():
        records[book] += 1
    else:
        records[book] = 1

# print(records)
# {'top': 4, 'kimtop': 1}

new_records = sorted(records.items())

# print(new_records)
# [('kimtop', 1), ('top', 4)]

best_sells = 0
best_seller = ''


for i in range(len(new_records)):
    if new_records[i][1] > best_sells:
        best_sells = new_records[i][1]
        best_seller = new_records[i][0]

print(best_seller)