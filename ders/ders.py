S1=int(input("Başlangış değerini giriniz: "))
S2=int(input("Son değeri giriniz: "))
inp=input("Tek sayı bulmak için tek çift sayı bulamk için çift komutunu giriniz: ")

if inp=="tek":
    for i in range(S1,S2+1,1):
        if i%2==1:
            print(i)
elif inp=="çift":
    for i in range(S1,S2+1,1):
        if i%2==0:
            print(i)
