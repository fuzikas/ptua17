import random
skaicius = random.randint(1,10)
print(skaicius)
spejimas = int(input("Atspek skaiciu nuo 1 iki 10 "))
if spejimas < skaicius:
    print("Per mazas, bandyk dar karta")
elif spejimas > skaicius:
    print("Per didelis, bandyk dar karta")
else:
    print(f"Teisingai! Skaicius buvo {skaicius}")