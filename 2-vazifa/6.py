class Inson:
    def __init__(self,ism,yosh):
        self.ism=ism
        self.yosh=yosh

class Talaba(Inson):
    def __init__(self, ism, yosh,universitet,baho):
        super().__init__(ism, yosh)
        self.universitet=universitet
        self.baho=baho

    def natija(self):
        if self.baho<0 or self.baho>100:
            print("Bunday baho mavjud emas!")
        elif self.baho>=86 and self.baho<=100:
            print("A'lo")
        elif self.baho>=71 and self.baho<=85:
            print("Yaxshi")
        elif self.baho>=56 and self.baho<=70:
            print("Qoniqarli")
        else:
            print("Qoniqarsiz")

talaba1 = Talaba("Ali", 20, "FDTU", 90)
talaba2 = Talaba("Vali", 21, "TATU", 60)
talaba3 = Talaba("Zilola", 19, "FDTU", 40)

talaba1.natija()
talaba2.natija()
talaba3.natija()
