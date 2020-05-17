
def nwd(x, y):
	return nwd(y, x%y) if y else x

#print nwd(6, 9)

class Ulamek:
	def __init__(self, licznik=0, mianownik=0):
		self.licznik = licznik
		self.mianownik = mianownik

	def wypisz(self):
		print(self.licznik)
		print("-")
		print(self.mianownik)

	def skroc(self):
		x = nwd(self.licznik, self.mianownik)
		self.licznik = self.licznik / x 
		self.mianownik = self.mianownik / x

	def wprowadz(self):
		self.licznik = input("wpisz licznik:")
		self.mianownik = input("wpisz mianownik:")
			
print("start")

x = Ulamek()
x.wprowadz()

dzialanie = raw_input("+lub-lub*")

y = Ulamek()
y.wprowadz()

x.wypisz()
print(dzialanie)
y.wypisz()
print("=")

wsp_mianownik = x.mianownik*y.mianownik

if dzialanie == "+":
	nowy_licznik = (x.licznik*y.mianownik) + (y.licznik*x.mianownik)

if dzialanie == "-":
	nowy_licznik = (x.licznik*y.mianownik) - (y.licznik*x.mianownik)

if dzialanie == "*":
	nowy_licznik = x.licznik*y.licznik

	
wynik = Ulamek(nowy_licznik, wsp_mianownik)
wynik.skroc()
wynik.wypisz()



