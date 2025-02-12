# Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.



def filtras():
    return  [i for i in range(1,1000) if i%6==0]

print(filtras())
