def asalSayiKontrol(sayi):
    if sayi <= 1:
        print("Lütfen 1'den büyük bir sayı giriniz.")
    for i in range(2,sayi):
        if sayi % i == 0:
            print(sayi, "asal bir sayı değildir.")
            return False
    print(sayi, "asal bir sayıdır.")

asalSayiKontrol(13)
asalSayiKontrol(15)
asalSayiKontrol(17)
asalSayiKontrol(21)
asalSayiKontrol(23)