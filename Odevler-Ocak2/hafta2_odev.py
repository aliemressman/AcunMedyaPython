# Konu: Karar yapıları (if-elif-else).

print("Lütfen bir sayı giriniz:")
sayi = int(input())

if sayi % 2 == 0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")
    
print("-----------------------------------------")

def not_hesapla(notu):
    if notu >= 90:
        print("A")
    elif notu >= 80:
        print("B")
    elif notu >= 70:
        print("C")
    elif notu >= 60:
        print("D")
    else:
        print("F")

print("Lütfen notunuzu giriniz:")
notu = int(input())
not_hesapla(notu)

print("-----------------------------------------")

def yas_aralik(yas):
    if yas <= 12:
        print("Çocuk")
    elif yas >= 13 & yas <= 19 :
        print("Genç")
    elif yas >= 20 & yas <= 59:
        print("Yetişkin")
    else:
        print("Yaşlı")

print("Lütfen yaşınızı giriniz:")
yas = int(input())
yas_aralik(yas)