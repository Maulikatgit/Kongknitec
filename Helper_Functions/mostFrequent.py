# Date    : 15/08/22 5:47 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0

def mostFrequent(arg):
    count = 0
    num = arg[0]
    for i in arg:
        curr_frequency = arg.count(i)
        if curr_frequency > count:
            count = curr_frequency
            num = i
    num = str(num)
    _, num = num.split('_')
    return num
