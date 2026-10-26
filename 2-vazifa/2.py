class Xodim:
    def __init__(self,ism,maosh):
        self.ism=ism
        self.maosh=maosh

    def malumot(self):
        print(f"Ism: {self.ism}, maosh: {self.maosh}")

class Oqituvchi(Xodim):
    def __init__(self, ism, maosh,fan):
        super().__init__(ism, maosh)
        self.fan=fan

    def malumot(self):
        super().malumot()
        print(f"Fan: {self.fan}")
    

class Farrosh(Xodim):
    def __init__(self, ism, maosh,qavat):
        super().__init__(ism, maosh)
        self.qavat=qavat

    def malumot(self):
        super().malumot()
        print(f"Qavat: {self.qavat}")

oqituvchi=Oqituvchi("Ali",10000000,"Python asoslari")
farrosh=Farrosh("Zilola",5000000,3)

oqituvchi.malumot()
farrosh.malumot()