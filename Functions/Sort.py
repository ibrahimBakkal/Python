a=[i for i in range(1,101)]
import random
random.shuffle(a)
def buble(x):
    count=0
    while count<=len(a)-1:
        for i in range(len(x)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                count=0
            else:
                count+=1
    return x