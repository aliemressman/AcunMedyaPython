class Human:
    # isim = "James"
    def __init__(self, isim):  # Yapıcı (constructor) metot
        self.isim = isim
        print("Bir Human örneği oluşturuldu")

    # return f"İnsan(isim={self.isim})"

    def __str__(self):  # Nesnenin string temsili
        return f"STR foknsiyonunda dönen değer: {self.isim})"

    def talk(self, sentence):
        print(f"{self.isim}: {sentence}")
        # self.walk()

    def walk(self):
        print(f"{self.isim} yürüyor")
