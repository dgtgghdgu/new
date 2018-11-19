# -*- conding:Utf-8 -*-
step = 1
def while_test(bigone):
    i = 1
    bigone_list=[]

    while i < bigone:
        print("This is the top:%s" % i)
        bigone_list.append(i)

        i += step

    return bigone_list


print(while_test(100))


