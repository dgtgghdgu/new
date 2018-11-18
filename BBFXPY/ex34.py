#-*- conding:Utf-8 -*-

animals = ['bear','python','peacock','kangaroo','whale','platypus']
numlist = ['1st','2nd','3rd','4th','5th','6th']

number = 0
for i in animals:
    print("The animal at %s is the %s and is a %s" % (number,numlist[number],i))
    number += 1
