import sys

sys.stdin = open('input1.txt')

w = input()

w_lst = 

for i in range(len(w)):


if len(w) % 2 == 1:
    
    min = 123
    tmp = 0
    lst = []

    for i in range(len(w)//2):
        if ord(w[i]) < min:
            min = ord(w[i])
    
    for i in range(len(w)//2):
        if ord(w[i]) == min:
            tmp += 1
            lst.append(i)

    
elif len(w) % 2 == 0:
    pass