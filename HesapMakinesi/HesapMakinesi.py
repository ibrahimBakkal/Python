try:
    s1=int(input("Birinci sayıyı giriniz: "))
    islem=input("İşlem seçiniz: (Çıkak için 'q' giriniz)")
    s2=int(input("İkinci Sayıyı giriniz: "))
    sonuc=0
    
    while islem!="q":

        if islem=="+":
            sonuc=s1+s2
            print(sonuc)
        elif islem=="-":
            sonuc=s1-s2
            print(sonuc)
        elif islem=="*":
            sonuc=s1*s2
            print(sonuc)
        elif islem=="/":
            sonuc=s1/s2
            print(sonuc)
        else:
            print("Lütfen bir işlem seçiniz")
        s1=sonuc
        islem=input("İşlem seçiniz: ")    
        s2=int(input("Sayı giriniz: "))
except:
    print("Lütfen Sayı Giriniz!")