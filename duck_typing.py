class Burung:
    def terbang(self):
        return "Burung terbang tinggi"


class Pesawat:
    def terbang(self):
        return "Pesawat lepas landas"


def uji_terbang(obj):
    print(obj.terbang())


b = Burung()
p = Pesawat()

uji_terbang(b)
uji_terbang(p)
