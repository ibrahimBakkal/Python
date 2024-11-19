# def BozanElamanIndeksi(Liste):
#     fark1 = []
#     fark2 = []
#     for i in range(1,len(Liste)):
#         fark1.append(Liste[i]-Liste[i-1])
#     for i in range(1,len(fark1)):
#         fark2.append(fark1[i]-fark1[i-1])        
#     indeks = 1
#     for i in fark2:    
#         if i!=0:
#             break
#         indeks+=1
        
#     return indeks+2
# # print(BozanElamanIndeksi([1,3,5,7,9,11,14]))
# def BasamakYıldız(sayi):
#     sayi=str(sayi)
#     kat=10**(len(sayi)-1)
#     for i in sayi:
#         a=int(i)
#         print(f"{i}    {a*"x"}")
#     kat=kat/10    
# # BasamakYıldız(1547)
# # sayılar=[]
# # for i in range(1,10):
# #     a=int(input(f"{i}. elemanın tabanı: "))
# #     a=a**int(input(f"{i}. elemanın üssü: "))
# #     sayılar.append(int(a))
# sayılar=[1,3,9,27,25,1,3,9,27]
# def ListeUsAynı(Liste):
#     yedek=list(Liste)
#     for n in Liste:
#         Liste[Liste.index(n)]=0
#         if  (n in Liste)==False:
#             Liste[yedek.index(n)]=n
#     print(Liste)
# ListeUsAynı(sayılar)
from Fonksiyon import Cekilis
Cekilis(5,1,2)

