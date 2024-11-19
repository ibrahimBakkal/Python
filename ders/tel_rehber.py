rehber={}
def num_ekle(etiket,numara):
    global rehber
    rehber[etiket]=numara
def num_sil(etiket):
    global rehber
    rehber.pop(etiket)
while True:
    com=input("numara eklemek için 1 \nsilmek için 2 \nkapatmak için 3")
    if com=="1":
        com1=input("İsim giriniz: ")
        com2=input("Numara giriniz: ")
        num_ekle(com1,com2)
    elif com=="2":
        com1=input("İsim giriniz: ")
        num_sil(com1)
    elif com=="3":
        print(rehber)
        break