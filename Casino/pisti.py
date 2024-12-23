import random
from os import system
system("cls")
oyuncu1=[]
oyuncu2=[]
oyuncu3=[]
oyuncu4=[]
kartlar=[]
orta=[]
oyuncu1puanlar=[]
oyuncu2puanlar=[]
oyuncu3puanlar=[]
oyuncu4puanlar=[]
    
for i in range(2,11):
    kartlar.append(f"Maça {i}")
kartlar.append("Maça As")
kartlar.append("Maça Vale")
kartlar.append("Maça Kraliçe")
kartlar.append("Maça Kral")

for i in range(2,11):
    kartlar.append(f"Kupa {i}")
kartlar.append("Kupa As")
kartlar.append("Kupa Vale")
kartlar.append("Kupa Kraliçe")
kartlar.append("Kupa Kral")

for i in range(2,11):
    kartlar.append(f"Karo {i}")
kartlar.append("Karo As")
kartlar.append("Karo Vale")
kartlar.append("Karo Kraliçe")
kartlar.append("Karo Kral")

for i in range(2,11):
    kartlar.append(f"Sinek {i}")
kartlar.append("Sinek As")
kartlar.append("Sinek Vale")
kartlar.append("Sinek Kraliçe")
kartlar.append("Sinek Kral")
random.shuffle(kartlar)
def dagıt():
    global oyuncu1
    global oyuncu2
    global oyuncu3
    global oyuncu4
    global kartlar
    for i in range(0,4):
        oyuncu1.append(kartlar[0])
        kartlar.pop(0)
    for x in range(0,4):
        oyuncu2.append(kartlar[0])
        kartlar.pop(0)
    for z in range(0,4):
        oyuncu3.append(kartlar[0])
        kartlar.pop(0)
    for c in range(0,4):
        oyuncu4.append(kartlar[0])
        kartlar.pop(0)
def kartat(oyuncu,sec):
    global oyuncu1
    global oyuncu2
    global oyuncu3
    global oyuncu4
    global kartlar
    global orta
    orta.append(oyuncu[sec])
    oyuncu.remove(oyuncu[sec])
def pistimi(oyuncu):
    global oyuncu1puanlar
    global oyuncu2puanlar
    global oyuncu3puanlar
    global oyuncu4puanlar
    global kartlar
    global orta
    for i in orta[-1]:
        if i==" ":
            try:
                son1=int(orta[-1][orta[-1].index(i)+1:])

            except:
                son1=(orta[-1][orta[-1].index(i)+1:])
    try:
        for i in orta[-2]:
            if i==" ":
                try:
                    son2=int(orta[-1][orta[-2].index(i)+1:])

                except:
                    son2=(orta[-2][orta[-2].index(i)+1:])
        if son1==son2: 
            for i in orta:
                oyuncu.append(i)
            orta.clear()                   
                    
    except:
        pass

        




tur=0
# kart=random.choice(kartlar)
# while tur<5:
#     if input("Tahmin Ediniz: ")==kart:
#         print("Kazandınız!!!!")
#         break

#     tur+=1
    
# if tur==5:
#     if "Maça" in kart or "Sinek" in kart:
#         print("Siyah")
#     elif "Kupa" in kart or "Karo" in kart:
#         print("Kırmızı")
        
# tur =0
# while tur<5:
#     if input("Tahmin Ediniz: ")==kart:
#         print("Kazandınız!!!!")
#         break
#     tur+=1
tur=0


while tur<4:
    if len(kartlar)==0:
        break
    dagıt()
    for i in range(0,4):
        print(oyuncu1)
        kartat(oyuncu1,int(input("Atmak İstediğiniz kartın sıra sayısını giriniz: "))-1)
        system("cls")
        print(orta[-1])
        pistimi(oyuncu1puanlar)
        print(oyuncu2)
        kartat(oyuncu2,int(input("Atmak İstediğiniz kartın sıra sayısını giriniz: "))-1)
        system("cls")
        print(orta[-1])
        pistimi(oyuncu2puanlar)
        print(oyuncu3)
        kartat(oyuncu3,int(input("Atmak İstediğiniz kartın sıra sayısını giriniz: "))-1)
        system("cls")
        print(orta[-1])
        pistimi(oyuncu3puanlar)
        print(oyuncu4)
        kartat(oyuncu4,int(input("Atmak İstediğiniz kartın sıra sayısını giriniz: "))-1)
        system("cls")
        print(orta[-1])
    
        
        
        
        
        
    tur+=1