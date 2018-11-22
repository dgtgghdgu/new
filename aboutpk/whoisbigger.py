# -*- conding:Utf-8 -*-
import random
import pandas as pd

class Player(object):
    def __init__(self):
        pass

    card = ""


def deal(serial, player) :
    serial_main =serial
    rnd_int = random.randint(0,(len(serial_main)-1))
    player_card = serial_main[rnd_int]
    del(serial_main[rnd_int])
    return serial_main,player_card

def showdown(p_card1,p_card2):
    if int(p_card1[1:]) > int(p_card2[1:]):
        win = p_card1
        winner = "player 1"
    elif int(p_card1[1:]) == int(p_card2[1:]):
        win = "Tie"
        winner = "Tie"
    else:
        win = p_card2
        winner = "Player 2"

    return win,winner
    


main_poker_serial = []
for i in range(13):
    for j in ["C","D","H","S"]:
        main_poker_serial.append(j+str(i+1))

print(main_poker_serial)
print(len(main_poker_serial))

#print("%s 获胜。\n赢家是 %s。" % (showdown(player_1.card,player_2.card)))

winner_count_list = []

for i in range(100):
    player_1 = Player()
    main_poker_serial,player_1_card = deal(main_poker_serial,player_1)

    player_2 = Player()
    main_poker_serial,player_2_card = deal(main_poker_serial,player_2)

    winner_count_list.append(showdown(player_1_card,player_2_card))

print(winner_count_list)

#winner_df = pd.DataFrame(winner_count_list)
#print(winner_df)