class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

class Savat:
    def __init__(self, nom):
        self.nom = nom
        self.mahsulotlar = []

    def mahsulot_qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar) 

    def __bool__(self):
        return len(self.mahsulotlar) > 0  

    def umumiy_narx(self):
        return sum(m.narx for m in self.mahsulotlar)  

    def __str__(self):
        return f"Savat nomi: {self.nom}, Mahsulotlar soni: {len(self.mahsulotlar)}"  


m1 = Mahsulot("Telefon", 3500000)
m2 = Mahsulot("Quloqchin", 300000)
m3 = Mahsulot("Noutbuk", 8500000)

savat = Savat("Mening savatim")
savat.mahsulot_qosh(m1)
savat.mahsulot_qosh(m2)
savat.mahsulot_qosh(m3)

if savat:
    print("Savat bo'sh emas!")
    print(savat)
    print("Umumiy narx:", savat.umumiy_narx(), "so'm")
else:
    print("Savat bo'sh[cite: 2].")