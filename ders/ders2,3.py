s=int(input("Bir sayı giriniz: "))
s1=int(s//10)
s2=int(s%10)
sonuc=1
for i in range(1,s1+1):
    sonuc*=i
print(f"Birler basamağının faktöriyeli {sonuc}")
sonuc=1
for i in range(1,s2+1):
    sonuc*=i
print(f"Birler basamağının faktöriyeli {sonuc}")