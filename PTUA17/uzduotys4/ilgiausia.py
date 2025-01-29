# Paprašyti vartotojo įvesties
input_numbers = input("Įveskite sveikuosius skaičius, atskirtus tarpais: ")
# Konvertuoti įvestį į sveikųjų skaičių sąrašą
numbers = []
for num in input_numbers.split():
    numbers.append(int(num))

longest_sequence = 1
current_sequence = 1

for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1] + 1:
        current_sequence += 1
    elif (
        numbers[i] != numbers[i - 1]
    ):  # Anuliuoti (reset) seką, jei nėra iš eilės einančio skaičiaus
        if current_sequence > longest_sequence:
            longest_sequence = current_sequence
        current_sequence = 1

# Galutinis palyginimas, tuo atveju, jeigu ilgiausia seka
# pasibaigia ties paskutiniu elementu
if current_sequence > longest_sequence:
    longest_sequence = current_sequence

print("Ilgiausios iš eilės einančių skaičių sekos ilgis yra:", longest_sequence)