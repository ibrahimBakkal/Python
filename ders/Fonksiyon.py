import random

def Cekilis(KisiSayi,AsilSayi,YedekSayi):
    Kisiler=list()
    Yedek=list()
    Asil=list()
    for i in range(1,KisiSayi+1):
        Kisiler.append(input(f"{i}. kişinin ismini giriniz: "))
    for i in range(1,AsilSayi+1):
        kisi=random.choice(Kisiler)    
        Asil.append(kisi)
        Kisiler.pop(Kisiler.index(kisi))

        # Kisiler.pop(Kisiler.index(i))
    for i in range(1,YedekSayi+1):
        kisi=random.choice(Kisiler)
        Yedek.append(kisi)
        Kisiler.pop(Kisiler.index(kisi))
    for i in range(1,len(Asil)+1):
        print(f"{i}. Asil {Asil[i-1]}")
    for i in range(1,len(Yedek)+1):
        print(f"{i}. Yedek {Yedek[i-1]}")

    