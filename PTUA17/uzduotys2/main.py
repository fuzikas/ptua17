number_one = int(input("Koks pirmas skaicius? "))
number_two = int(input("Koks antras skaicius? "))

if number_one > number_two:
    print("Pirmas didesnis uz antra")
elif number_one < number_two:
    print("Antras didesnis uz pirma")
elif number_two == number_one:
    print("lygus")