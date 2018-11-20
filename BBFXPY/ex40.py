# -*- conding:Utf-8 -*-

class song(object):

    def __init__(self,lyrics):
        self.lyrics =lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


cat_lyc = ["我们一起学猫叫","一起喵喵喵喵喵","在你面前撒个娇","哎呦喵喵喵喵喵",
"我的心脏砰砰跳","迷恋上你的坏笑","你不说爱我我就喵喵喵"]

champion = ["I've paid my dues",
            "Time after time",
            "I've done my sentence",
            "But committed no crime",
            "And bad mistakes",
            "I've made a few",
            "I've had my share of sand kicked in my face",
            "But I've come through"]
happy_bday = song(["happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = song(["They rally around tha family",
                        "with pockets full of shells"])

we_are_champion =song(champion)

cat_study = song(cat_lyc)

happy_bday.sing_me_a_song()
print("*" * 30)
bulls_on_parade.sing_me_a_song()
print("*" * 30)
cat_study.sing_me_a_song()
print("*" * 30)
we_are_champion.sing_me_a_song()