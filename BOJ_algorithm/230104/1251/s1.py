import sys

sys.stdin = open('input3.txt')

w = input()

# print(w)

w_lst = []

for i in range(len(w)):
    w_lst.append(ord(w[i]))
# print(w_lst)
# [109, 111, 98, 105, 116, 101, 108]

result_lst = []

# 단어를 돌려서 단어를 대체할 리스트를 만들고, 기존의 것과 바꿔주기
for i in range(1, len(w_lst) -1):
    for j in range(i + 1, len(w_lst)):


        front = w[0:i]
        center = w[i:j]
        back = w[j:len(w_lst)]

        # print(front, center, back)
        # m o bitel
        # m ob itel
        # m obi tel
        # m obit el
        # m obite l
        # mo b itel
        # mo bi tel
        # mo bit el
        # mo bite l
        # mob i tel
        # mob it el
        # mob ite l
        # mobi t el
        # mobi te l
        # mobit e l 
       
        tmp_lst = []

        for k in range(-1, -len(front) -1, -1):
            tmp_lst.append(ord(front[k]))
        for k in range(-1, -len(center) -1, -1):
            tmp_lst.append(ord(center[k]))
        for k in range(-1, -len(back) -1, -1):
            tmp_lst.append(ord(back[k]))

        # print(tmp_lst)
        # [109, 111, 108, 101, 116, 105, 98]
        # [109, 98, 111, 108, 101, 116, 105]
        # [109, 105, 98, 111, 108, 101, 116]
        # [109, 116, 105, 98, 111, 108, 101]
        # [109, 101, 116, 105, 98, 111, 108]
        # [111, 109, 98, 108, 101, 116, 105]
        # [111, 109, 105, 98, 108, 101, 116]
        # [111, 109, 116, 105, 98, 108, 101]
        # [111, 109, 101, 116, 105, 98, 108]
        # [98, 111, 109, 105, 108, 101, 116]
        # [98, 111, 109, 116, 105, 108, 101]
        # [98, 111, 109, 101, 116, 105, 108]
        # [105, 98, 111, 109, 116, 108, 101]
        # [105, 98, 111, 109, 101, 116, 108]
        # [116, 105, 98, 111, 109, 101, 108]

        if result_lst == []:
            result_lst = tmp_lst
        else:
            for k in range(len(result_lst)):
                if tmp_lst[k] > result_lst[k]:
                    break
                elif tmp_lst[k] == result_lst[k]:
                    continue
                else:
                    result_lst = tmp_lst
                    break

result = ''

for i in range(len(result_lst)):
    result += chr(result_lst[i])

print(result)