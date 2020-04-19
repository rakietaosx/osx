lass Ulamek:
	def __init__(self, licznik=0, mianownik=0):
		self.licznik = licznik
		self.mianownik = mianownik

	def wypisz(self):
		print(self.licznik)
		print("-")
		print(self.mianownik)


x = Ulamek(3,1)
x.wypisz()
print("-")
y=Ulamek(2,1)
y.wypisz()
print("=")

wsp_mianownik = x.mianownik*y.mianownik

nowy_licznik = (x.licznik*y.mianownik) - (y.licznik*x.mianownik)

suma = Ulamek(nowy_licznik, wsp_mianownik)

suma.wypisz()
