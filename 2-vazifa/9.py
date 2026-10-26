class Karta:
    def __init__(self,egasi, raqam_oxiri,balans):
        self.egasi=egasi
        self.raqam_oxiri=raqam_oxiri
        self.balans=balans

    def __str__(self):
        balans=f"{self.egasi:,}".replace(","," ")
        return f"Egasi: {self.egasi} , balans: {balans}"

    def __gt__(self, other):
        return self.balans>other.balans

    def __lt__(self, other):
        return self.balans<other.balans


karta1=Karta("Ali",1234,50000)
karta2=Karta("Vali",5678,52000)

if karta1>karta2:
    print(f"{karta1.egasi}ning kartasida mablag koproq")
elif karta1<karta2:
    print(f"{karta2.egasi}ning kartasida mablag koproq")
else:
    print(f"Ikkala kartada mablag teng")