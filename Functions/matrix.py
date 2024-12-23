import random

def rastgele(row,col):
    return [[random.randint(0,9) for i in range(col)] for i in range(row)]
def yazdır(matris):
    for i in matris:
        print(i)
def birim(n):
    m=sıfır(n,n)
    for i in range(len(m)):
        m[i][i]=1
    return m
 
def sıfır(row,col):
    return [[0 for i in range(col)] for i in range(row)]

def topla(a,b):
    sonuc=sıfır(len(a),len(a[0]))
    for row in range(len(a)):
        for eleman in range(len(a[row])):
            sonuc[row][eleman]=a[row][eleman]+b[row][eleman]
    return sonuc
def temizle():
    import os
    os.system("cls")
def olustur():
    a=int(input("Sütun sayısını giriniz:"))
    b=int(input("Satır sayısını giriniz:"))
    m=[]
    for i in range(a):
        x=[]
        for c in range(b):
            x.append(input(f"{i+1}.satır {c+1}.eleman için değer giriniz:"))
        m.append(x)
        x=[]
    return m

def kare(matris):
    c=matris
    # for  i in range(len(matris)):
    #     for b in range(len(matris[i])):
    #         c[i][b]=c[i][b]**2
    
    return c
