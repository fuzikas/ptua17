

# class Auto:
#     def __init__(self, name, country, reliable):
#         self.name = name
#     def get_name(self):
#         return self.name
#     def is_semi(self):
#         return False
    

# class Semi(Auto):
#     def is_semi(self):
#         return True
    

# glock = Semi("glock")
# ak = Auto("ak")
# m4 = Auto("m4")
# walther = Semi("walther")

# print(m4.get_name(), m4.is_semi())


class Gun:
    def __init__(self, name:str, country:str, is_realiable:bool):
        self.name = name
        self.country = country
        self.is_reliable = is_realiable

class Auto(Gun):
    def __init__(self, is_cheap):
        self.is_cheap = is_cheap

    def guns_data(self):
        super().__init__("ak", "russia", True)
        print(f"Name: {self.name}, Country of origin: {self.country}, Reliable: {self.is_reliable}, Cheap: {self.is_cheap}")




my_guns = Auto(False)
my_guns.guns_data()

