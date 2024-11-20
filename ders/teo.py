# a=int(input("Bir sayı giriniz: "))
# if a>0:
#     print("Sayı pozitif")
# elif(a<0):
#     print("Sayı negatif")
# elif a==0:
#     print("Sayı 0")
# b=0
# c=[]
# while b!=3:
#     b+=1
#     a=int(input("Bir sayı giriniz: "))
#     c.append(a)
# c.sort()
# c.reverse()
# print(c)


T1=-1
T2=1
for i in range(-5,5,6):
    T1=T1+2*i
    
    for j in range(5,1,-3):
        T1=T1-2*j
        T2=T2-i
    T2=T2+i
print(f"[{T1}],[{T2}]")