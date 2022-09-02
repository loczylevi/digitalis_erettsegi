print("1. feladat")
bekeres = int(input("Fordulók száma: "))
print()
print("2. feladat")
szamlalo = 0
lista = []
while True:
    if szamlalo < bekeres:
        bekeres2 = int(input(f"{szamlalo+1}. fordulóban a gólkülönbség: "))
        lista.append(bekeres2)
        szamlalo = szamlalo + 1
    else:
        break

print()
print("3. feladat")

gyozelem = 0
vereseg = 0
dontetlen = 0

for gol in lista:
    if gol > 0:
        gyozelem = gyozelem + 1
    elif gol == 0:
        dontetlen = dontetlen + 1
    else:
        vereseg = vereseg + 1

print(f"A szezonban a csapatnak {gyozelem} győzelme, {vereseg} veresége, {dontetlen} döntetlene volt.")


print()
print("4. feladat")
print(f"A csapatnak a szezonban összesen {(gyozelem*3)+(dontetlen*1)} pontja lett.")

