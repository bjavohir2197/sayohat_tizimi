class Sayohatchi:
    def __init__(self, ism):
        self.ism = ism
        self.manzillar = []

    def manzil_qosh(self, manzil):
        self.manzillar.append(manzil)

    def sayohatlar_soni(self):
        return len(self.manzillar)


sayohatchi1 = Sayohatchi("Ali")
sayohatchi1.manzil_qosh("Toshkent")
sayohatchi1.manzil_qosh("Samarqand")

print(f"Sayohatchi: {sayohatchi1.ism}")
print(f"Manzillar: {sayohatchi1.manzillar}")
print(f"Sayohatlar soni: {sayohatchi1.sayohatlar_soni()}")
