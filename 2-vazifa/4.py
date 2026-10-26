class Shakl:
    def yuza(self):
        return 0

class Kvadrat(Shakl):
    def __init__(self,tomon):
        self.tomon=tomon

    def yuza(self):
        return self.tomon**2

class Torgitortburchak(Shakl):
    def __init__(self,eni,boyi):
        self.eni=eni
        self.boyi=boyi

    def yuza(self):
        return self.eni*self.boyi

shakllar=[Kvadrat(7),Torgitortburchak(5,6)]

for shakl in shakllar:
    print(shakl.yuza())