adet=int(input("Sepetteki ürün adedi:"))
top=adet*15
if top<50 and top>0 :
    top+=7
    print(f"Toplam ücret {top}")
elif top>=50:
    print(f"Kargonuz ücretsiz ve toplam üretiniz {top}")
elif top<0:
    print("Lütfen geçerli bir sayı giriniz")
