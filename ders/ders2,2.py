s=int(input("Bir sayı giriniz: "))
for i in range(0,3):
    if i ==0:
        print(f"{(s%100)%10} sayının birler basamağıdır.")
    if i ==0:
        print(f"{int(((s%100)-(s%100)%10)/10)} sayının onlar basamağıdır.")
    if i ==0:
        print(f"{s//100} sayının yüzler basamağıdır.")