my_name = '石头'
my_age = 38
my_height = 170 #cm
my_weight = 95 #kg
my_eyes = '黑色'
my_teeth = '白色'
my_hair = '黑色'

print("我叫%s。" % my_name)
print("身高%d厘米." % my_height)
print("体重%dkg 。"% my_weight)
print("真的是太胖了。")
print("眼睛是%s的,头发是%s 。"%( my_eyes,my_hair))
print("牙是%s的但是常常有茶渍。" % my_teeth)
# 这一行是试试，看看能不能正常的出现
print("如果我长高到%d,体重降低到%d公斤,年龄减小到%d,我就会%d。"
      % (my_height+10,my_weight-25,my_age-10,my_age+my_height+my_weight))