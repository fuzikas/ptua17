suma = 0

for i in range(10):
    number = int(input(f"Iveskite sveikaji skaiciu{i+1}:"))
    suma +=number
vidurkis = suma/10
print(f"Suma: {suma}, Vidurkis: {vidurkis}")