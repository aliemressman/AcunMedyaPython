# Konu: Listeler, Tuple'lar, listelerde döngü.

liste = []

for i in range(5):
    sayilar = int(input("Lütfen bir sayı giriniz:"))
    liste.append(sayilar)

print(liste)
toplam = sum(liste)
ortalama = toplam / len(liste)
en_buyuk = max(liste)
en_kucuk = min(liste)

print("-----------------------------------------")

print("kelime giriniz:")
kelime1 = input()
kelime2 = input()
kelime3 = input()

liste2 = [kelime1, kelime2, kelime3]
print(liste2)
liste2.reverse()
print(liste2)

print("-----------------------------------------")

liste3 = [1, 2, 3, 4, 5, 4, 4, 8, 5, 10]
new_list = set(liste3)
print(new_list)