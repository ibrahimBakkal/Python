import random
kelimeler = [
"eşya", "ördek", "çiftlik", "çocuk", "şehir", "şarkı", "ışık", 
"güneş", "kızıl", "beyaz", "kale", "köprü", "göl", "dağ", "yazı", "deniz", 
"kapı", "çatı", "halı", "ev", "bahçe", "kuzu", "kitap", "kalem", "defter", 
"sözlük", "harita", "kavun", "karpuz", "şeftali", "biber", "soğan", "muz", 
"nar", "böcek", "uçurtma", "taş", "insan", "dostluk", "sevgi", "umut", 
"barış", "özgürlük", "gözlük", "tabela", "ışıldak", "şemsiye", "cüzdan", 
"pantolon", "gömlek", "kedi", "köpek", "kaplumbağa", "tilki", "tavşan", 
"kuş", "balık", "yunus", "karga", "serçe", "leylek", "eşek", 
"inek", "horoz", "arı", "karınca", "çorap", "ayakkabı", "çanta", "kazak", 
"atkı", "eldiven", "şapka", "mont", "takvim", "saat", "radyo", "televizyon", 
"bilgisayar", "cep", "telefon", "kamera", "mikrofon", "pencere", "ayna", 
"bıçak", "kaşık", "çatal", "tabak", "bardak", "evren", "yıldız", 
"galaksi", "gezegen", "ay", "dünya", "okyanus", "nehir", "akarsu", "orman", 
"ağaç", "çimen", "çiçek", "kar", "yağmur", "fırtına", "rüzgar", "bulut", 
"şimşek", "gökkuşağı", "şeker", "çikolata", "dondurma", "bisküvi", 
"kek", "pasta", "tatlı", "kahve", "çay", "limonata", "bal", "zeytin", 
"peynir", "yoğurt", "ekmek", "pilav", "makarna", "lahana", "ıspanak", 
"domates", "patates", "salatalık", "kabak", "havuç", "sarımsak", 
"bezelye", "mercimek", "nohut", "fındık", "ceviz", "badem", "kestane", 
"üzüm", "erik", "kiraz", "çilek", "vişne", "kayısı", "ananas", "mango", 
"avokado", "incir", "arı", "kelebek", "örümcek", "akrep", 
"yılan", "kurbağa", "kaplan", "aslan", "zebra", "zürafa", "fil", "maymun", 
"ayı", "penguen", "yunus", "köpekbalığı", "kaplumbağa", "kartal", 
"şahin", "atmaca", "baykuş", "güvercin", "serçe", "bülbül", "keklik", 
"kırlangıç", "leylek", "martı", "turna",   "istakoz", 
"balina", "ahtapot", "denizatı", "denizyıldızı", "mercanköşk", "yosun", 
"salyangoz", "midye", "denizkabuğu", "kalamar", "karides", "kurbağa", 
"ördek", "kaz",  "kartal", "tilki", "kurt", "ayı", "çakal", 
"sincap", "kirpi", "tavşan", "gelincik", "samur", "kunduz", "fare", 
"sıçan", "kirpi", "tavuk", "horoz", "güvercin", 
"kanarya", "papağan",  "kartal", "atmaca",  "flamingo", 
"zürafa", "zebra", "hipopotam", "kaplan", "aslan", "fil", "maymun", 
"koala", "kanguru", "panda", "yılan", "kertenkele", "timsah", "bukalemun", 
"kek", "şeker", "çorba", "lahmacun", "pide", "börek", "kebap", 
"salata", "pizza", "hamburger", "sandviç",  "kumpir", 
"baklava", "kadayıf", "tiramisu", "pasta",  "muhallebi", "sütlaç"]
kelime=random.choice(kelimeler)
harfler=list()
for i in kelime:
    harfler.append(i)
cizgi=list()
for i in range(len(kelime)):
    cizgi.append("_")


hak=6
while hak!=0:
    print(hak)
    inp=input("Harf giriniz: ")
    if inp in kelime:
        for i in range(0,len(kelime)):
            if inp==kelime[i]:
                cizgi[i]=inp
    else:
        hak-=1
    if inp==kelime:
        print(kelime)
    elif inp=="pes ediyorum":
        print(kelime)
        break
    else:
        temp=cizgi.copy()
        temp="".join(temp)
        print(temp)
    if temp==kelime:
        print("Kazandın!!!!!!!!")
        break
    elif inp==kelime:
        print("Kazandın!!!!!!!!")
        break       
if hak==0:
    print(kelime)
    