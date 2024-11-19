s=int(input("Bir sayı giriniz: "))
s1=int(s//10)
s2=int(s%10)
print(s1)
print(s2)
if s1 > s2:
    print(f"{s1} {s2}")
elif s2>s1:
    print(f"{s2} {s1}")
