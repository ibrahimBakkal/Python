users_passwords={"admin":"1234","user1":"1234","user2":"1234"}
status={"admin":False,"user1":False,"user2":False}
print("Kullanıcı eklemek için ekle\nKullanıcı silmek için sil\nGiriş yapmak için giriş\nÇıkış yapmak çıkış\nUygulamayı kapatmak için kapat komutlarını kullanınız.")
print("Kullanıcı silmek için ya admin olarak giriş yapmış olmalısınız yada silmek istediğiniz kullanıcının şifresini doğru girmelisiniz.")
com=""
inp1=""
inp2=""
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
        inp1=input("Kullanıcı adınızı giriniz: ")
        inp2=input("Şifrenizi giriniz: ")
        
        if users_passwords[inp1]==inp2:
            status[inp1]=True
        else:
            print("Kullanıcı adınızı veya şifrenizi yanlış girdiniz.")
    elif com=="çıkış":
        inp1=input("Çıkış yapmak istediğiniz kullanıcıyı giriniz: ")
        status[inp1]=False
print(users_passwords)
print(status)
            
                
            
            
        
        