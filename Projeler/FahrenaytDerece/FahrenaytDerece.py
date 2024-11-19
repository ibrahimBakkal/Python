fahr=input("Lütfen fahrenayt cinsinden dereceyi giriniz: ")
try:
    inp=float(fahr)
    celsius=(fahr-32.0)*5.0/9.0
    print(celsius)
except:
    print("Lütfen bir sayı giriniz")