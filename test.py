import random #进口随机
y = random.randint(1,100) #计算机＝随机
print(y)

while True: #真正的
    x = int(input("请输入100以内的整数：")) #x=int(1-100)
    print(x)
    if(x>y): #如果（x>计算机）
        print("大了") #打印（大了）
    elif(x<y): #elif（x<计算机）
        print("小了") #打印（小了）
        
    else: #其他
        print("恭喜你赢了") #打印（恭喜你赢了）
        break #打破