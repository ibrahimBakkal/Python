# def DigitalSaat(Saat,Dakika,Saniye):
#     Liste=[]
#     count=1
#     Liste.append(f"{Saat}.{Dakika}.{Saniye}")
#     while count<=4:
#         Saniye+=1
#         if Saniye==60:
#             Saniye=0
#             Dakika+=1
#         if Dakika==60 :
#             Dakika=0
#             Saat+=1
#         if Saat==24:
#             Saat=0
        
#         count+=1
#         Liste.append(f"{Saat}.{Dakika}.{Saniye}")
#     return Liste
# print(DigitalSaat(12,59,58))

# def ListeyiOlustur(baslangic,bitis):
#     Liste=[]
#     nums=[]
#     for i in range(baslangic,bitis+1):
#         nums.append(i)
#     for i in nums:
#         if i%3==0:
#             Liste.append(i)
#     return Liste
# print(ListeyiOlustur(15,25))

# def RasgeleSayiliListeUret(baslangic,bitis,adet):
#     pass
# print(RasgeleSayiliListeUret(10,15,5))
        
    
# def YerDegis(Liste):
#     if len(Liste)%2==0:
#         for i in range(0,len(Liste)-1,2):
            
#             Liste[i],Liste[i+1]=Liste[i+1],Liste[i]
#     return Liste
# print(YerDegis([0,1,2,3,4,5,6,7,8,9]))
# def BasVeSonHarfiBuyut(cumle):

#Baş ve Son harf büyütme

def BasVeSonHarfiBuyut(cumle):
    kelimeler=cumle.split()
    karakter=[]
    sonuc=[]
    son=""
    kelime=""
    print(kelimeler)
    for i in kelimeler:
        karakter=list(i)
        print(karakter)
        karakter[0]=chr(ord(i[0])-32)
        karakter[-1]=chr(ord(i[-1])-32)
        kelime="".join(karakter)
        sonuc.append(kelime)
        son=" ".join(sonuc)
    return son
print(BasVeSonHarfiBuyut("merhaba bugün programlama dersinin vize sınavındayız"))



# def RasgeleSayiliListeUret(baslangic,bitis,adet):
#     import random
#     count=0
#     Liste=[]
#     nums=[]
#     for i in range(baslangic,bitis+1):
#         nums.append(i)
#     while count!=adet:
#         count+=1
#         Liste.append(random.choice(nums))
#     return Liste
# print(RasgeleSayiliListeUret(5,7,5)) 

# def BozanElamanIndeksi(Liste):
#     doubles={}
#     artıslar=[]
#     for n in range(0,len(Liste)-1):
#         doubles[Liste[n]]=Liste[n+1]
#     for i in doubles.items():
#         artıslar.append(i[1]-i[0])
#     if artıslar[0]==artıslar[1] and artıslar[1]==artıslar[2] :
#         artıs=artıslar[0]
#     elif artıslar[0]==artıslar[1] and artıslar[0]==artıslar[2]:
#         artıs=artıslar[0]
#     print(artıs)
            
# BozanElamanIndeksi([1,3,5,6,9,11,13])