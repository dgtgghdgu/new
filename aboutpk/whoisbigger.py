# -*- conding:Utf-8 -*-
import random

class Player(object):
    def __init__(self):
        pass

    def get_card(self,count):
        #随机获得一张点数
        rand_int = random.randint(1,count)
        return rand_int

    def show_card(self,cards):
        print("底牌：")

def whoisbig(p1,p2):
    pass


def deal(serial,player):
    serial_main =serial
    rnd_int = random.randint(1,len(serial_main))
    player_card = serial_main[rnd_int]
    del(serial_main[rnd_int])
    return serial_main,player_card

main_poker_serial = []


for i in range(13):
    for j in ["C","D","H","S"]:
        main_poker_serial.append(j+str(i+1))

print(main_poker_serial)
print(len(main_poker_serial))
print("*" *30)

#main_poker_serial_ready = random.shuffle(main_poker_serial)

#print(main_poker_serial_ready)

player_1 = Player()
main_poker_serial,player_1_card = deal(main_poker_serial,player_1)


print(len(main_poker_serial),main_poker_serial)
print("*" *30)
print(player_1_card)
print("*" *30)

player_2 = Player()
main_poker_serial,player_2_card = deal(main_poker_serial,player_2)

print("*" *30)
print(player_2_card)
print("*" *30)

