def hesapMakinesi(sayi,sayi2,islem):
    if islem == "+":
        print(sayi + sayi2)
    elif islem == "-":
        print(sayi - sayi2)
    elif islem == "*":
        print(sayi * sayi2)
    elif islem == "/" or islem == "//":
        if sayi2 == 0:
            print("Bir sayıyı 0'a bölemezsiniz.")
        else:
            if islem == "//":
                print(sayi // sayi2)
            else:
                print(sayi / sayi2)
    else:
        print("Geçersiz işlem.")

hesapMakinesi(5,3,"+")
hesapMakinesi(5,3,"-")
hesapMakinesi(5,3,"*")
hesapMakinesi(5,3,"/")
hesapMakinesi(5,3,"//")
hesapMakinesi(5,0,"/")
