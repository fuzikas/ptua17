pirmas = float(input("Ivesk pirma skaiciu "))
simbolis = input("Iveskite simboli (+, -, *, /) ")
antras = float(input("Ivesk antra skaiciu "))
if simbolis == "+":
    print(f"{pirmas} + {antras} rezultatas yra {pirmas+antras}")
elif simbolis == "-":
    print(f"{pirmas} - {antras} rezultatas yra {pirmas-antras}")
elif simbolis == "*":
    print(f"{pirmas} * {antras} rezultatas yra {pirmas*antras}")
elif simbolis == "/":
    print(f"{pirmas} / {antras} rezultatas yra {pirmas/antras}")
elif simbolis != "+" or "/" or "+" or "-" or "*":
    print("ne toks simbolis")
#else:
   # print("kazkas ne taip, turbut ne ta simboli ivedei?")