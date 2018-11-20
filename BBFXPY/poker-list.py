#-*- conding:Utf-8 -*-

#写一个列表，放入表示扑克牌的52张牌（不包含大小王牌）
#C代表club梅花，D代表diamond方块，S代表spade黑桃，H代表heart红心，1-13分别代表A-K,
poker_list = []
kind_list =["C","D","H","S"]

for i in kind_list:
    for j in range(13):
        poker_list.append(i + str(j+1))

print(poker_list)
print(type(poker_list))
print(len(poker_list))
print(type(poker_list[0]))
