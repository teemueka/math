from tabulate import tabulate
import math

print(1)
value_1a = math.degrees(2.493)
value_1b = math.degrees(0.911)
print(f"1 a) {value_1a:.2f} astetta", f" b) {value_1b:.2f} astetta")

value_2a = math.radians(137.7)
value_2b = math.radians(62.3)
print(f"2 a) {value_2a:.2f} radiaania", f" b) {value_2b:.2f} radiaania")

print("3 Kulmat radiaaneina")

degrees = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
data = []

for degree in degrees:
    radians = math.radians(degree)
    data.append([degree, radians])

headers = ["asteet", "radiaanit"]
print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

#2
#Suorakulmaisen kolmion kateetit ovat pituudeltaan 2,3 ja 4,7.
#Määritä hypotenuusan pituus sekä kolmion kaksi muuta kulmaa asteina.
print(2)
kateetti1 = 2.3
kateetti2 = 4.7
hypotenuusa = math.sqrt(kateetti1**2 + kateetti2**2)
print("hypotenuusan pituus: "f"{hypotenuusa:.2f}")

kulma1 = math.degrees(math.asin(kateetti1 / hypotenuusa))
kulma2 = math.degrees(math.asin(kateetti2 / hypotenuusa))

print(f"Kulma 1: {kulma1:.2f} astetta")
print(f"Kulma 2: {kulma2:.2f} astetta")

#3
#Laske math-kirjastoa käyttäen seuraavien lukujen kertoma: 0, 4, 7, 15
print(3)
print("luvun 0 kertoma:", math.factorial(0))
print("luvun 4 kertoma:", math.factorial(4))
print("luvun 7 kertoma:", math.factorial(7))
print("luvun 15 kertoma:", math.factorial(15))


