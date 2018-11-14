from sys import argv
script,filename = argv
txt = open(filename)

print("Here's your file %r:"% filename)
print(txt.read())

print("请再次输入文件名：")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())