for sayi in range(2,101):
    asal=True
    for i in range(2,sayi):
        if sayi%i==0:
            asal=False
    if asal==True:
        print(sayi)
        