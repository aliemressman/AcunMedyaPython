# Konu: Fonksiyonlar, parametreler, return.

def hesapMakinesi(sayi1 ,sayi2):
    print("Toplama için 1, Çıkarma için 2, Çarpma için 3, Bölme için 4 giriniz:")
    secim = int(input())
    if secim == 1:
        sonuc = sayi1 + sayi2
        print(sonuc)
    elif secim == 2:
        sonuc = sayi1 - sayi2
        print(sonuc)
    elif secim == 3:
        sonuc = sayi1 * sayi2
        print(sonuc)
    elif secim == 4:
        sonuc = sayi1 / sayi2
        print(sonuc)
    else:
        print("Hatalı giriş yaptınız.")

hesapMakinesi(5, 3)

print("-------------------------------------------------")

def palindrom(s):
    if s == s[::-1]:
        print("Palindromdur.")
    else:
        print("Palindrom değildir.")

palindrom("kazak")
palindrom("merhaba")

print("-------------------------------------------------")

def yas100(yas):
    kalan = 100 - yas
    print("100 yaşına gelmenize", kalan, "yıl kaldı.")

yas100(25)