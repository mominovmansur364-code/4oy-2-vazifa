class Kitob:
    def __init__(self,nom, muallif, sahifa_soni):
        self.nom=nom
        self.muallif=muallif
        self.sahifa_soni=sahifa_soni

    def malumot(self):
        print(f"Nomi: {self.nom}, muallifi: {self.muallif}, sahifalar soni: {self.sahifa_soni}")

class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni,format,fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format=format
        self.fayl_hajmi=fayl_hajmi

    def malumot(self):
        super().malumot()
        print(f"Formati: {self.format}, fayl hajmi: {self.fayl_hajmi} MB ")


kitob = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 350)
e_kitob = ElektronKitob("Mehrobdan chayon", "Abdulla Qodiriy", 300, "pdf", 4.5)

kitob.malumot()
e_kitob.malumot()