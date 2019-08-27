# 引用随机
import random

# 计算机＝随机
y = random.randint(1, 100) 
print(y)

# 永久的循环
while True: 
    x = int(input("请输入100以内的整数：")) 
    print(x)
    if (x > y):
        print("大了")
    elif (x < y):
        print("小了")
    else: 
        print("恭喜你赢了")
        break
