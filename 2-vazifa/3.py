class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda")


class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda g'ildiraklar yordamida yurmoqda")


class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedallar yordamida harakatlanmoqda")


class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd relslar bo'ylab harakatlanmoqda")


transportlar = [Mashina(), Velosiped(), Poyezd()]

for t in transportlar:
    t.harakatlanish()