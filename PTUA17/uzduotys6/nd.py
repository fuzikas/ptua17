
weight = int(input("Enter your weight in KGs "))
height = float(input("Enter you height in meters "))



def bmi(weight, height):
    bmi = weight/(height**2)
    rounded = round(bmi, 2)
    print(rounded)

bmi(weight, height)

