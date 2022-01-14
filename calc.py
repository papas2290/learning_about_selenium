# import math
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))


flag = 0

sum = 5

while flag != 1:
    if sum < 5:
        sum += 1
        print(sum)
    else:
        flag = 1
        print('ok')
