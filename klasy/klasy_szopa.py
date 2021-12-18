class Szopa:
    def __init__(self, bok_a, bok_b, wys_h): #konstruktor klasy, wlacza sie jako pierwszy przy uruchomieniu klasy
        self.podstawa_a = bok_a
        self.podstawa_b = bok_b
        self.wysokosc_h = wys_h
    
    def pomaluj(self):
        return 2*(self.podstawa_a * self.podstawa_b) * self.wysokosc_h

szopa1 = Szopa(2,3,5)
print(szopa1.pomaluj())
szopa2 = Szopa(5,1,2)
print(szopa2.pomaluj())