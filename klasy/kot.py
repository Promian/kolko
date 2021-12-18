class kot:
    def __init__(self): #konstruktor klasy, wlacza sie jako pierwszy przy uruchomieniu klasy
        self.imie = ""
        self.kolor_oczu = ""
        self.kolor_siersci = ""
        self.dlugosc = 0
        self.wysokosc = 0
        self.wiek = 0
        self.waga = 2

    def miauczenie():
        print("Miau!")
    
    def spanie(self):
        if self.wiek <= 10 and self.wiek >0:
            print('śpi 10 godzin')
        elif self.wiek > 10:
            print('śpi 12 godzin')

    def jedzenie(self):
        self.waga += 1
        print('kot dobrze zjadl')

    def drapanie(self):
        if self.waga <= 10:
            print("Straty są znikome")
        else:
            print("kot zniszczył wszystko")



        
