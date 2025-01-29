sarasas = []
while True:
        ats = input("Skaicius ar pabaiga? ")
        if ats!="pabaiga":
                sarasas.append(float(ats))
        elif ats == "pabaiga":
                print("Programa baigta")
                break
            
ilgis = len(sarasas)
average = sum(sarasas) / ilgis
average = round(average, 1)
print(f"Skaiciai: {sarasas}")
print(f"Vidurkis yra: {average}")