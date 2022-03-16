import sys

sys.stdin = open('4874_Forth_input.txt')

T = int(input())

for tc in range(1, T+1):
    test = list(map(str, input().split()))

    nums = []
    for i in range(len(test)):
        if test[i].isnumeric() == True:
            nums.append(int(test[i]))
        else:
            if len(nums) >= 2:
                num1 = nums.pop()
                num2 = nums.pop()
                if test[i] == '+':
                    nums.append(num2+num1)
                elif test[i] == '-':
                    nums.append(num2-num1)
                elif test[i] == '*':
                    nums.append(num2*num1)
                elif test[i] == '/':
                    nums.append(int(num2/num1))
                else:
                    print(f'#{tc} error')
                    break
            else:
                if test[i] == '.':
                    print(f'#{tc} {nums[0]}')
                else:
                    print(f'#{tc} error')
                    break