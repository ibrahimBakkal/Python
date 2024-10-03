ogr=input("Adınızı Soyadınız giriniz:")
nmr=input("Öğrenci numaranızı giriniz: ")
vize=input("Vİze notunuzu giriniz:")
final=input("Final notunuzu giriniz: ")
ort=int(vize)*0.4+int(final)*0.6
if int(final)>=55 and ort>=40:
    print("İnönü üniversitesi öğrenci "+nmr+" numaralı "+ogr+"'ın ortalaması "+str(ort)+"dır\nŞartlı olarak dersten geçmiştir.")
elif int(final)>=55 and ort>=45:
    print("İnönü üniversitesi öğrenci "+nmr+" numaralı "+ogr+"'ın ortalaması "+str(ort)+"dır\nDersten geçmiştir.")
else:
    print("dersten kaldınız")
