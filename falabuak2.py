print("1. feladat")
fordulok = int(input("Fordulók száma: "))

print("")
print("2. feladat")
lista =  []
for szam in range(fordulok):
  bekeres = int(input(f"{szam+1}. fordulóban a gólkülömbség: "))
  lista.append(bekeres)

gyoztes = len([pont for pont in lista if pont > 0]) 

vesztes = len([pont for pont in lista if pont < 0])

dontetlen = len([pont for pont in lista if pont == 0])
#[2, 3, 0, 1, -3]
print(f"3. feladat")
print(f"A szezonban a csapatnak {gyoztes} győzelme, {vesztes} veresége, {dontetlen} döntetlene volt.")

print("")
print(f"4. feladat")
print(f"A csapatnak a szezonban összesen {gyoztes*3+dontetlen*1} pontja lett.")

eggyut = vesztes + dontetlen
print("")
print(f"5. feladat")
if gyoztes > eggyut:
  print("A csapatnak több győztes mérkőzése volt, mint veresége és döntelene együttvéve.")
else:
  print("A csapatnak kevesebb győztes mérkőzése volt, mint veresége és döntelene együttvéve.")

#[2, 3, 0, 1, -3]
  
"""
A csapat céljai között szerepelt, hogy egy mérkőzésen több góllal győzzenek, mint az
előző győztes(!) mérkőzésen! Vizsgálja meg, és a mintának megfelelően jelezze,
hogy a csapat hányszor érte el ezt a célt a szezonban!
"""

print("")
print("6. feladat")
siker = 0
szamlalo = 0 
for szam in lista:
  if szam > szamlalo and szamlalo > 0:
    siker += 1
  szamlalo = szam
    

print(f"A kitűzött célt {siker} alkalommal sikerült elérnie a csapatnak.")


