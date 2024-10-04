import pickle


print("Kullanıcı eklemek için ekle\nKullanıcı silmek için sil\nGiriş yapmak için giriş\nÇıkış yapmak çıkış\nUygulamayı kapatmak için kapat komutlarını kullanınız.")
print("Kullanıcı silmek için ya admin olarak giriş yapmış olmalısınız yada silmek istediğiniz kullanıcının şifresini doğru girmelisiniz.")
com=""
inp1=""
inp2=""


with open("status.pkl","rb") as f:
    status=pickle.load(f)
with open("users_passwords.pkl","rb") as f:
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
        try:
            if status["admin"]==True:
                users_passwords.pop(inp1)
                status.pop(inp1)
            else:
                print("Kullanıcı silmek admin olarak giriş yapmış olmalısınız.")
        except:
            if users_passwords[inp1]==users_passwords.keys():
                inp2=input("Silmek istediğiniz kullanıcının şifresini giriniz: ")
                users_passwords.pop(inp1)
                status.pop(inp1)
            else:
                print("Silmek istediğiniz kullanıcının şifresini doğru girmelisiniz.")
        

    elif com=="çıkış":
        inp1=input("Çıkış yapmak istediğiniz kullanıcıyı giriniz: ")
        status[inp1]=False
    elif com=="giriş":
        inp1=input("Kullanıcı adınızı giriniz: ")
        inp2=input("Şifrenizi giriniz: ")
        if users_passwords[inp1]==inp2:
            status[inp1]=True
        else:
            print("Kullanıcı adınızı veya şifrenizi yanlış girdiniz.")
    with open("users_passwords.pkl","wb") as f:
        pickle.dump(users_passwords, f)
    with open("status.pkl","wb") as f:
        pickle.dump(status,f)

print(users_passwords)
print(status)
            
                
            
            
        
        