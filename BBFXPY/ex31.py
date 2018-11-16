# -*- conding:Utf-8 -*-
print("这里有两扇深色的大门，1号和2号，你选哪一个？只按数字")

door =  input(">")
if door == "1":
    print("你看到一头巨大的熊正在吃奶酪蛋糕，你要怎么办")
    print("1、带走这个蛋糕")
    print("2、吓走这只熊")

    bear = input("请输入你的选择：")
    if bear == "1":
        print("熊没有饭吃了，只有吃了你，哈哈哈")
    elif bear =="2":
        print("熊掉头来追你，抓掉了你的胳膊，你完了")
    else:
        print("好吧，你的%s选择救了你，熊看了你一眼，被吓跑了。" % bear)

elif door =="2":
    print("你看到了像一双恶魔的眼睛在盯着你，你认为是什么东西")
    print("1、蓝莓")
    print("2、黄色夹克衫")
    print("3、可以理解为疯狂的东西")
    insanity = input("请输入你的选择：")
    if insanity == "1" or insanity == "2":
        print("你被恶魔吸干了，变成了僵尸")
    else:
        print("你被扔到一口烂水池里，里面有各种腐烂的东西")

else:
    print("你掉下去了，倒在一把刀上，挂了")


print("真是一个痛苦的游戏。。。。。。。。")
