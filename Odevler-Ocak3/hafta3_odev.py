# Konu: For ve while döngüleri.

def ilk_100_sayi():
    i = 1
    while i <= 100:
        print(i)
        i += 1
    
print("-----------------------------------------")

def cift_sayilar():
    i = 1
    while i <= 100:
        if i % 2 == 0:
            print(i)
        i += 1

print("-----------------------------------------")

def faktoriyel_hesapla(sayi):
    print("deger giriniz:")
    sayi = int(input())
    faktoriyel = 1
    while sayi >= 1:
        faktoriyel *= sayi
        sayi -= 1
    print(faktoriyel)

faktoriyel_hesapla(5)

print("-----------------------------------------")

sayi = int(input("Lütfen bir sayı giriniz:"))
i = 2

while i < sayi:
    if sayi % i == 0:
        print("Girdiğiniz sayı asal değildir.")
        break
    else:
        print(sayi,"asal bir sayıdır.")
        break
