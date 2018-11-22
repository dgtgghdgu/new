# -*- conding_Utf-8 -*-

import random
import pandas as pd

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

class Player(object):
    def __init__(self):
        pass

    card = ""

def deal(serial) :
    serial_main =serial
    rnd_int = random.randint(0,(len(serial_main)-1))
    deal_card = serial_main[rnd_int]
    del(serial_main[rnd_int])
    return serial_main,deal_card

def bigger():

    main_poker_serial = []
    for i in range(13):
        for j in ["C", "D", "H", "S"]:
            main_poker_serial.append(j + str(i + 1))

    main_poker_serial,player_1_card = deal(main_poker_serial)

    main_poker_serial,player_2_card = deal(main_poker_serial)

    return showdown(player_1_card,player_2_card)

winner_count_list = []
for i in range(10000):
    winner_count_list.append(bigger())

df_count_winner = pd.DataFrame(winner_count_list)

df_count_winner.to_csv("winer10000.csv")

print(df_count_winner)
print(df_count_winner.info())





