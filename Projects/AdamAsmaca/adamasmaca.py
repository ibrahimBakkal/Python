import random
kelimeler=["elma", "armut","muz","portakal","şeftali","kiraz","çilek"]
kelime=random.choice(kelimeler)
harfler=list()
for i in kelime:
    harfler.append(i)
cizgi=list()
for i in range(len(kelime)):
    cizgi.append("_")

hak=len(kelime)
while hak!=0:
    print(hak)
    inp=input("Harf giriniz: ")
    if inp in kelime:
        for i in range(0,len(kelime)):
            if inp==kelime[i]:
                cizgi[i]=inp
    else:
        hak-=1
    temp=cizgi.copy()
    temp="".join(temp)
    print(temp)
    if temp==kelime:
        print("Kazandın!!!!!!!!")
        break
    