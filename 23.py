#引用随机
import random 

print('--------1--------')
x = input('不妨猜下我现在心里想的什么数字吧')
y = int(x)

#h = 随机一个1-100的整数
h = random.randint(1, 100)

while y != h:
    x = input("哎呀，猜错咯，请重新输入")
    y = int(x)
    if y == h:
        print("我去，你是我心里的蛔虫吗？！")
        print("哼，猜中了也没用奖励！")
    else:
        if y > h:
            print("嘿，大了，大了")
        else:
            print("嘿，小了，小了")

print("游戏结束，不玩啦︿(￣︶￣)︿")
