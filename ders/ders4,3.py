try:
    tc=input("TC'nizi giriniz: ")
    tc_eleman=[]
    a=0
    while a<=10:
        tc_eleman.append(int(tc[a]))
        a+=1
    tek=tc_eleman[0]+tc_eleman[2]+tc_eleman[4]+tc_eleman[6]+tc_eleman[8]
    cift=tc_eleman[1]+tc_eleman[3]+tc_eleman[5]+tc_eleman[7]
    hane10=((tek*7)-cift)%10

    if hane10!=tc_eleman[9]:
        print("Geçersiz TC ")
    elif hane10==tc_eleman[9]:
        top=tc_eleman[0]+tc_eleman[1]+tc_eleman[2]+tc_eleman[3]+tc_eleman[4]+tc_eleman[5]+tc_eleman[6]+tc_eleman[7]+tc_eleman[8]+tc_eleman[9]
        hane11=top%10
        if hane11!=tc_eleman[10]:
            print("Geçersiz TC ")
        else:
            print("Geçerli TC ")

except:
    print("Lütfen sadece rakam giriniz")

    