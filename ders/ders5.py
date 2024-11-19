# VKİ hesaplama
# boy=int(input("Boyunuzu giriniz: "))
# boy =boy/100
# kilo=int(input("Kilonuzu giriniz: "))
# vki=kilo/(boy**2)
# print(f"Vücut kütle endeksiniz {vki}dir")
# nums=[]
# num=input("Bir sayı giriniz: ")
# top=0
# while True:
#     num=input("Bir sayı giriniz: ")
#     if num!="q":    
        
#         nums.append(int(num))
#     elif num=="q":
#         break
    
# for i in nums:
#     top=top+i
# print(f"Aritmetik ortalama {top/len(nums)}")
cumle=input("Cümlenizi girniz: ")
kelime=input("bulmak istediğiniz kelimeyi giriniz: ")
kelimeler=[]
kelimeler=cumle.split(" ")
for i in kelimeler:
    if i==kelime:
        print(f"Kelimeniz bulundu, {i} ve cümlenizin {kelimeler.index(i)+1}. kelimesi")