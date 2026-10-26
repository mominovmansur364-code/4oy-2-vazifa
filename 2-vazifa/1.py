class Hayvon:
    def __init__(self,nomi,yoshi):
        self.nomi=nomi
        self.yoshi=yoshi

    def ovoz(self):
        print(f"{self.nomi} ovoz chiqarmoqda")

class It(Hayvon):
    def __init__(self, nomi, yoshi):
        super().__init__(nomi, yoshi)

    def qoriqlash(self):
        print(f"{self.nomi} qoriqlamoqda")

class Mushuk(Hayvon):
    def __init__(self, nomi, yoshi):
        super().__init__(nomi, yoshi)

    def sichqon_tutish(self):
        print(f"{self.nomi} sichqon tutmoqda")


it=It("Reks",3)
mushuk=Mushuk("Mosh",2)

it.ovoz()
mushuk.ovoz()

it.qoriqlash()
mushuk.sichqon_tutish()
