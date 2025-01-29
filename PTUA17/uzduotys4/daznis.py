symbols = input("Iveskite simboliu eilute ")
my_dict = {}

for i in (symbols):
    if i in my_dict:
        my_dict[i] +=1
    else:
        my_dict[i] = 1
print(my_dict)

for i, freq in sorted(my_dict.items()):
    print(f"{i}: {freq}")