# -*- encoding:utf-8 -*-

import random

random_numer = random.randint(0,100)
print(random_numer)

# input_number = raw_input("请输入一个数：")
# print("user input a number：%s" % input_number)

i = 0
while True:
    input_number = int(input("请输入一个数："))
    if input_number == random_numer:
        print("恭喜你猜对了")
        break
    elif input_number > random_numer:
        print ("猜大了")
    else:
        print ("猜小了")
    i += 1

