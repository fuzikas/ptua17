

class Gun:
    def __init__(self, name:str, country:str, is_realiable:bool, is_cheap:bool):
        self.name = name
        self.country = country
        self.is_reliable = is_realiable
        self.__where_to_buy = "Go to afghanistan"
        self.is_cheap = is_cheap

    def guns_data(self):
        print(f"Name: {self.name}, Country of origin: {self.country}, Reliable: {self.is_reliable}, Cheap: {self.is_cheap}")
        

class Auto(Gun):
    def __init__(self):
        super().__init__("AK", "russia", True, False)

class Semi(Gun):
    def __init__(self):
        super().__init__("Glock", "Belgium", True, True)

        pass




my_guns = Auto()
my_guns.guns_data()

glock = Semi()
glock.guns_data()

