# 猜数字游戏
import random
answer = random.randint(1,100)
while True:
    num = int(input("请输入猜的数字"))
    if num == answer:
        print("恭喜猜对了")
        break
    elif num > answer:
        print("猜大了")
    else :
        print("猜小了")