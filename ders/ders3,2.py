fahr=int(input("Lütfen fahrenayt cinsinden dereceyi giriniz: "))

inp=float(fahr)
celsius=(fahr-32.0)*5.0/9.0
if celsius<=15 and -459.67<=fahr:
    print(f"Hava soğuk ve {celsius} derece.")
elif 15<=celsius<=25 and -459.67<=fahr:
    print(f"Hava ılık ve {celsius} derece.")
elif celsius>25 and -459.67<=fahr:
    print(f"Hava sıcak ve {celsius} derece.")
else:
    print("Lütfen geçerli bir sıcaklık değeri giriniz.")