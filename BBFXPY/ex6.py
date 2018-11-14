x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)
print(x)
print(y)

print("我说:%r" % x)
print("我还说：%s." % y)

hilarious = False
#变量hilarious 变量赋值
joke_evaluation =  "Isn't that joke so funny?! %r"
#带转义符的字符串赋值给变量joke_evaluation

print(joke_evaluation % hilarious) #打印出用转义符输出的两个变量

w = "This is the left side of ..."  #赋值给w变量一个字符串
e = "a string with a right side."   #赋值给e变量一个字符串

print(w + e)




