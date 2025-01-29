my_dictionary = {"Vardas":"Antanas", "Amzius":12, "Miestas": "Siauliai"}
print(my_dictionary["Miestas"])

my_dictionary["Miestas"] = "Klaipeda"
print(my_dictionary)

del my_dictionary["Vardas"]
print(my_dictionary)
amziai = my_dictionary.pop("Amzius")
print(amziai)
print(my_dictionary)