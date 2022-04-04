import sys

sys.stdin = open('4880_input.txt')

# 원리 앞에서 부터 2명씩 대결 후 리스트에 추가... 홀수라면 어차피 마지막 친구는 부전승

def win(cards):
    lst = []
    while cards:
        if len(cards) == 1:
            if lst:
                lst.append(cards[0])
                cards[1:]
                return (win(lst))
            else:
                return cards[0][0]
        else:
            a = cards.pop(0)
            b = cards.pop(0)
            # print(a, b)
            if a[1] == b[1]:
                lst.append(a)
            elif a[1] == 1 and b[1] == 2:
                lst.append(b)
            elif a[1] == 1 and b[1] == 3:
                lst.append(a)
            elif a[1] == 2 and b[1] == 3:
                lst.append(b)
            elif a[1] == 2 and b[1] == 1:
                lst.append(a)
            elif a[1] == 3 and b[1] == 1:
                lst.append(b)
            elif a[1] == 3 and b[1] == 2:
                lst.append(a)
            cards[2:]
    return win(lst)

T = int(input())

for tc in range(1, T + 1):
    # 인원 수 == N
    N = int(input())
    # cards == N명이 보낸 카드가 번호 순으로 주어짐
    cards = list(map(int, input().split()))

    for i in range(0, N):
        cards[i] = [i+1, cards[i]]  # 인덱스 번호와 함께 추가
    # print(cards)
    # [[1, 1], [2, 3], [3, 2], [4, 1]]

    print(f'#{tc} {win(cards)}')
    # 1 3
    # 2 5
    # 3 1




