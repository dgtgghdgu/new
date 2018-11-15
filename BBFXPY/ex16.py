from sys import argv
script,filename = argv

print("We're going to earse %r." % filename)
print("If you don't want that,hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

print("?")

print("Open the file...")
target = open(filename,"w")

print("Truncating the file. goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(str(line1))
target.write("\n")
target.write(str(line2))
target.write("\n")
target.write(str(line3))
target.write("\n")

print("And finally,we close it.")
target.close()
nr = open(filename)
print(nr.read())