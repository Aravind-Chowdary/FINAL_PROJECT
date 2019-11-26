from random import randrange
f = open("rands.txt", "w+")
num=100000
i=0
while i<num:
    m=randrange(0,65536)
    f.write('%d \n' %m)
    i +=1
f.close()