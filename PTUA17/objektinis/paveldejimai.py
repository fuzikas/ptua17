

class Gun:
    def __init__(self, name:str, country:str, is_realiable:bool, is_cheap:bool):
        self.name = name
        self.country = country
        self.is_reliable = is_realiable
        self.__where_to_buy = "Go to afghanistan"
        self.is_cheap = is_cheap

    def main_data(self):
        print(f"Name: {self.name}, Country of origin: {self.country}, Reliable: {self.is_reliable}, Cheap: {self.is_cheap}")
        

class Auto(Gun):
    def __init__(self, name, country, is_reliable, is_cheap, is_old):
        self.is_old = is_old
        super().__init__(name, country, is_reliable, is_cheap)

    def sub_data(self):
        print(f"Name: {self.name}, Country of origin: {self.country}, Reliable: {self.is_reliable}, Cheap: {self.is_cheap}, Old: {self.is_old}")

class Semi(Gun):
    def __init__(self, name, country, is_reliable, is_cheap, mag_size):
        self.mag_size = mag_size
        super().__init__(name, country, is_reliable, is_cheap)
    def sub_data(self):
        print(f"Name: {self.name}, Country of origin: {self.country}, Reliable: {self.is_reliable}, Cheap: {self.is_cheap}, Magazine capacity: {self.mag_size}")




auto_gun = Auto("AK", "russia", True, False, True)
auto_gun.sub_data()
auto_gun.main_data()

semi_gun = Semi("Glock", "Belgium", True, True, 15)
semi_gun.sub_data()
semi_gun.main_data()

# glock = Semi()
# glock.guns_data()

