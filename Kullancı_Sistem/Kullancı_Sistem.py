import pickle


print("Kullanıcı eklemek için ekle\nKullanıcı silmek için sil\nGiriş yapmak için giriş\nÇıkış yapmak çıkış\nUygulamayı kapatmak için kapat komutlarını kullanınız.")
print("Kullanıcı silmek için o kulanıcıda oturum açmış yapmış olmalısınız.")
com=""
inp1=""
inp2=""


with open("Kullancı_Sistem/status.pkl","rb") as f:
    status=pickle.load(f)
with open("Kullancı_Sistem/users_passwords.pkl","rb") as f:
    users_passwords=pickle.load(f)

while com!="kapat":
    
    com=input("Ne yapmak istediğinizi giriniz: ")
    if com=="ekle":
        inp1=input("Kullanıcı adı giriniz: ")
        inp2=input("Şifre giriniz: ")
        users_passwords[inp1]=inp2
        status[inp1]=False
    elif com=="sil":
        inp1=input("Silmek istediğiniz kullanıcının kullanıcı adını giriniz: ")
        if status["admin"]==True or status[inp1]==True:
            users_passwords.pop(inp1)
            status.pop(inp1)
        else:
            print("Silmek istediğiniz kullanıcıda oturum açmış olmalısınız.")
        

    elif com=="çıkış":
        inp1=input("Çıkış yapmak istediğiniz kullanıcıyı giriniz: ")
        status[inp1]=False
    elif com=="giriş":
        for i in status.keys():
            status[i]=False
        inp1=input("Kullanıcı adınızı giriniz: ")
        inp2=input("Şifrenizi giriniz: ")
        if users_passwords[inp1]==inp2:
            status[inp1]=True
        else:
            print("Kullanıcı adınızı veya şifrenizi yanlış girdiniz.")
for i in status.keys():
    status[i]=False            
with open("Kullancı_Sistem/users_passwords.pkl","wb") as f:
    pickle.dump(users_passwords, f)
with open("Kullancı_Sistem/status.pkl","wb") as f:
    pickle.dump(status,f)


                
            
            
        
        
