def buble(x):
    import random
    random.shuffle(x)
    count=0
    while count<=len(x)-1:
        for i in range(len(x)-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
                count=0
            else:
                count+=1
    return x
