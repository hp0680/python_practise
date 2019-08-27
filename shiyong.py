print('--------1--------')
temp = input('不妨猜下我现在心里想的什么数字吧')
guess = int(temp)

import random
computer=random.randint(1,1000)

number=int(input("请输入1000以内的整数："))

while True:
  
    guess = int(temp)
    if guess == True:
        print("我去，你是我心里的蛔虫吗？！")
        print("哼，猜中了也没用奖励！")
    else:
        if guess > True:
             print("嘿，大了，大了")
        else:
             print("嘿，小了，小了")

print("游戏结束，不玩啦︿(￣︶￣)︿")
