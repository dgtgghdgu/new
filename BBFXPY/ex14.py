from sys import argv
script, user_name = argv
prompt = "："

print("你好%s, 我是%s脚本。" % (user_name,script))
print("我想问你几个问题。")
print("你喜欢我不 %s" % user_name)
likes = input(prompt)

print("住在哪里呢%s" % user_name)
lives = input(prompt)

print("你用的是哪个型号的电脑")
computer = input(prompt)

print("""好吧, 你说你%r喜欢我。
你在%r住， 不过我不确定。
你还有%s电脑，真牛逼。""" % (likes,lives,computer))