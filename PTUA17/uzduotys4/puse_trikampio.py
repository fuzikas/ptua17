size = int(input("Įveskite trikampio dydį: "))

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # pereiname į naują eilutę
