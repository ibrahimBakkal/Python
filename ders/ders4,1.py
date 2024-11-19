import math
a=int(input("Öğrenci sayısı giriniz: "))
b=0
c=[]
art=0
d=0
while b<=a-1:
    c.append(int(input("Öğrenci notlarını teker teker giriniz:")))
    b+=1
for i in c:
    art=art+i
art=art/a
for i in c:
    d=d+(art-i)**2
print(f"Standart sapma {math.sqrt(d/(a-1))}")
    
    