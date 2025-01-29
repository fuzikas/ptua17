#skaiciuoklis
#pirmas = int(input("Iveskite pirma skaiciu "))
#antras = int(input("Iveskite antra skaiciu "))

#print(pirmas+antras)


#temp converteris
#farenheitas = int(input("Įveskite temperatūrą pagal Farenheitą  "))
#celsijus = (farenheitas-32) *5/9
#suapvalintas_celsijus= round(celsijus, 1)
#print(f"Temperatūra pagal Celsijų: {suapvalintas_celsijus}")


#zodzio apvertejas
#zodis = input("Įveskite žodį ")

#print(f"Apverstas žodis: {zodis[::-1]} ")

#vardo_formatavimas
#name = input("Įveskite savo vardą  ")
#surname = input("Įveskite savo pavardę  ")
#print(f"Formatuotas vardas: {surname}, {name}")


#palukanu skaiciuokle
#pradine = int(input("Iveskite pradine suma: "))
#palukanu_norma = int(input("Iveskite palukanu norma (%): "))
#laikas = int(input("Iveskite laika metais"))
#print(f"Paprastosios palukanos yra {(pradine*palukanu_norma*laikas)/100}")

#Asmeninis pasisveikinimas
pilnas_vardas = input("Įveskite savo pilną vardą:  ")
sutvarkytas_vardas = pilnas_vardas.split()
print(f"Labas, {sutvarkytas_vardas[0]}, sveiki atvykę!")