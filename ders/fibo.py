fibo=[1,1]
n=int(input("n değerni giriniz: "))
n-=2
top=0
for i in range(n):
    print(fibo[i])
    top=top+fibo[i]+fibo[i+1]
    print(f"q{top}q")
    fibo.append(fibo[i]+fibo[i+1])
print(fibo)
print(top)



