class Zwierze:
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga
    
    def podaj_dane(self):
        print(f'Jestem zwierzeciem {self.nazwa}, mam {self.wiek} lat i ważę {self.waga} kg.')

class Slon(Zwierze):
    pass

class Lew(Zwierze):
    def __init__(self):
        self.ilosc_klow = 4

class Papuga(Zwierze):
    def __init__(self, nazwa,dlg_skrzydel):
        self.ilosc_pior = 800
        self.nazwa = nazwa
        self.dlg_skrzydel = dlg_skrzydel

class Hybryda(Lew, Papuga):
    pass

hyb = Hybryda()
hyb.ilosc_klow = 4
hyb.nazwa = "HUHUHS"
hyb.waga = 100
hyb.ilosc_pior = 300
hyb.wiek = 34

hyb.podaj_dane()

Dumbo = Slon("Slonik Dumbo", 300, 4)

Simba = Lew()
Simba.ilosc_klow = 3
Simba.wiek = 34
Simba.nazwa = "Lew Simba"
Simba.waga = 450

Simba.podaj_dane()
Dumbo.podaj_dane()