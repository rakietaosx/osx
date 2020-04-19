import random


print("witaj w grze")
hp = 0
while True:

	liczba1 = random.randint(10,90000)
	liczba2 = random.randint(10,90000)

	print("masz %d punktow. ile to jest %d + %d ?" %(hp,liczba1, liczba2))

	liczba = input("wpisz wynik")

	if liczba == liczba1+liczba2:
		print("dobrze")
		hp=hp+1
	else:

		print("fail. mialo byc %d" % (liczba1+liczba2))
		break

	
