print("kodlamaio")

# değişkenAdı = değer(int, float, string, boolean)
baslik = "Taşıt Kredisi"  # string => metinsel ifade

print(baslik)

baslik = "İhtiyaç Kredisi"  # string => metinsel ifade

print(baslik)

vade = 36  # int => tam sayı
ekVade = 6  # int => tam sayı
vade2 = "36"  # string => metinsel ifade

aylikÖdeme = 200.50  # float => ondalıklı sayı

yukselisteMi = False  # boolean => true veya false

# Matematiksel Operatörler

# + => toplama
print(5 + 5)  # 10
print(vade + 12)  # 48
print(vade + ekVade)  # 42
print(36 + 6)  # 42

# - => çıkarma
print(5 - 5)  # 0
print(vade - 12)  # 24
print(vade - ekVade)  # 30
print(36 - 6)  # 30

# * => çarpma
print(5 * 5)  # 25
print(vade * 12)  # 432
print(vade * ekVade)  # 216
print(10 * 10)  # 100

# / => bölme
print(5 / 5)  # 1.0
print(vade / 2)  # 18.0
print(vade / ekVade)  # 6.0
print(10 / 2)  # 5.0

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)  # 18.0
print(indirimliFiyat)  # 80

# % => mod
print(10 % 2)  # 0
print(vade % 5)  # 1
print(vade % ekVade)  # 0
print(30 % 10)  # 0

# Boolean Operatörler

# == => eşit mi
print(1 == 1)  # True
print(1 == 2)  # False

# > => büyüktür
print(1 > 2)  # False
print(3 > 1)  # True
print(1 > 1)  # False
print(1 >= 1)  # True

# < => küçüktür
print(1 < 2)  # True
print(3 < 1)  # False
print(1 < 1)  # False
print(1 <= 1)  # True

# != => eşit değildir
print(1 != 1)  # False
print(1 != 2)  # True

# veya => or
# bir tanesi doğruysa doğru sonuç döner
print(1 > 2 or 5 > 2)  # (false or true) => true
print(1 > 2 or 5 > 2 and 3 > 2)  # (false or true and true) => true
print(1 > 2 and 5 > 2 and 3 > 2)  # (false and true and true) => false
print(2 > 1 or 1 > 2 and 3 > 2)  # (true or false and true) => true

# Karar Yapıları
# ve => and
# her ikisi de doğru olmalı ki doğru sonuç gelsin
print(1 > 2 and 5 > 2)  # (false and true) => false

# If (Eğer) Durumu

# if (koşul):
#     kod bloğu

sayi1 = 10
sayi2 = 15

if sayi1 < sayi2:
    print("sayi1, sayi2'den büyüktür")
    print("if bloğunun içindeyim")
elif sayi1 == sayi2:
    print("sayi1, sayi2'ye eşittir")
    print("elif bloğunun içindeyim")
else:
    print("sayi2, sayi1'den büyüktür")
    print("else bloğunun içindeyim")

print("if bloğunun dışında")

if sayi1 <= sayi2:
    print("sayi1, sayi2'ye eşit veya küçüktür")
if sayi1 == sayi2:
    print("sayi1, sayi2'ye eşittir")
else:
    print("sayi2, sayi1'den büyüktür")

print("**************************")
# sonuç => sayi1, sayi
#2'ye eşit veya küçüktür, sayı1 sayi
#2'ye eşittir

if sayi1 < sayi2:
    print("sayi1, sayi2'ye eşit veya küçüktür")
    if sayi1 == sayi2:
        print("sayi1, sayi2'ye eşittir")
else:
    print("sayi2, sayi1'den büyüktür")
# sonuç => sayi
#2, sayi1'den büyüktür
