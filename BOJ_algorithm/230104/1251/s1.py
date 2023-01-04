import sys

sys.stdin = open('input2.txt')

w = input()

w_lst = []

for i in range(len(w)):
    w_lst.append(ord(w[i]))
# print(w_lst)
# [109, 111, 98, 105, 116, 101, 108]

# 단어를 돌려서 단어를 대체할 리스트를 만들고, 기존의 것과 바꿔주기
if len(w) % 2 == 1:

    tmp_lst = []
    
    for i in range(1, len(w)//2 + 1):
        tmp_lst = []
        front = w[0:i]
        center = w[i:len(w)-i]
        back = w[len(w)-i:len(w)]
        
        # print(front, center, back)
        # m obite l
        # mo bit el
        # mob i tel

        for j in range(-1, -len(front) -1, -1):
            tmp_lst.append(ord(front[j]))
        
        # print(tmp_lst)
        # [109]
        # [111, 109]
        # [98, 111, 109]
        
        for j in range(-1, -len(center) -1, -1):
            tmp_lst.append(ord(center[j]))

        # print(tmp_lst)
        # [109, 111, 98, 105, 116, 101]
        # [111, 109, 98, 105, 116]
        # [98, 111, 109, 105]
        
        for j in range(-1, -len(back) -1, -1):
            tmp_lst.append(ord(back[j]))

        # print(tmp_lst)
        # [109, 111, 98, 105, 116, 101, 108]
        # [111, 109, 98, 105, 116, 108, 101]
        # [98, 111, 109, 105, 108, 101, 116]

        for j in range(len(w_lst)):
            if tmp_lst[j] > w_lst[j]:
                break
            elif tmp_lst[j] == w_lst[j]:
                continue
            else:
                w_lst = tmp_lst
                break

        # print(w_lst)
        # [109, 111, 98, 105, 116, 101, 108]
        # [109, 111, 98, 105, 116, 101, 108]
        # [98, 111, 109, 105, 108, 101, 116]
    
elif len(w) % 2 == 0:
    tmp_lst = []
    
    for i in range(1, len(w)//2):
        tmp_lst = []
        front = w[0:i]
        center = w[i:len(w)-i]
        back = w[len(w)-i:len(w)]
        
        # print(front, center, back)
        # m obite l
        # mo bit el
        # mob i tel

        for j in range(-1, -len(front) -1, -1):
            tmp_lst.append(ord(front[j]))
        
        # print(tmp_lst)
        # [109]
        # [111, 109]
        # [98, 111, 109]
        
        for j in range(len(center)):
            tmp_lst.append(ord(center[j]))

        # print(tmp_lst)
        # [109, 111, 98, 105, 116, 101]
        # [111, 109, 98, 105, 116]
        # [98, 111, 109, 105]
        
        for j in range(-1, -len(back) -1, -1):
            tmp_lst.append(ord(back[j]))

        # print(tmp_lst)
        # [109, 111, 98, 105, 116, 101, 108]
        # [111, 109, 98, 105, 116, 108, 101]
        # [98, 111, 109, 105, 108, 101, 116]

        for j in range(len(w_lst)):
            if tmp_lst[j] > w_lst[j]:
                break
            elif tmp_lst[j] == w_lst[j]:
                continue
            else:
                w_lst = tmp_lst
                break

result = ''

for i in range(len(w_lst)):
    result += chr(w_lst[i])

print(result)