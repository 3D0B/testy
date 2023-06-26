import uuid


class HulajnogaElektryczna:
    def wyswietl_informacje(self):
        pass


class Hulajnoga5km(HulajnogaElektryczna):
    def __init__(self, kod_modelu):
        self.kod_modelu = kod_modelu

    def wyswietl_informacje(self):
        return f"Hulajnoga elektryczna 5km, kod modelu: {self.kod_modelu}"


class Hulajnoga10km(HulajnogaElektryczna):
    def __init__(self, kod_modelu):
        self.kod_modelu = kod_modelu

    def wyswietl_informacje(self):
        return f"Hulajnoga elektryczna 10km, kod modelu: {self.kod_modelu}"


class Hulajnoga15km(HulajnogaElektryczna):
    def __init__(self, kod_modelu):
        self.kod_modelu = kod_modelu

    def wyswietl_informacje(self):
        return f"Hulajnoga elektryczna 15km, kod modelu: {self.kod_modelu}"


class FabrykaHulajnog:
    def __init__(self):
        self.produkty = []

    def utworz_hulajnoge(self, typ):
        kod_modelu = str(uuid.uuid4())[:8]
        if typ == "5km":
            hulajnoga = Hulajnoga5km(kod_modelu)
        elif typ == "10km":
            hulajnoga = Hulajnoga10km(kod_modelu)
        elif typ == "15km":
            hulajnoga = Hulajnoga15km(kod_modelu)
        else:
            print("Nieznany typ hulajnogi: " + typ)
            return None

        self.dodaj_produkt(hulajnoga)  
        return hulajnoga

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt)

    def wyswietl_produkty(self):
        for produkt in self.produkty:
            print(produkt.wyswietl_informacje())


fabryka = FabrykaHulajnog()

while True:
    pytanie = input("co chcesz zrobić? wybierz opcje (1.wyprodukować hulajnoge. 2.pokaż listę wyprodukowanych hulajnóg): ")

    if pytanie == "1":
        wybor = input("Wybierz rodzaj hulajnogi (5km, 10km, 15km): ")
        hulajnoga = fabryka.utworz_hulajnoge(wybor)
        
        print(hulajnoga.wyswietl_informacje())

    elif pytanie == "2":
        fabryka.wyswietl_produkty()

    else:
        print("Nieznana opcja")
