

class Gun:
    def __init__(self, name:str, country:str, is_realiable:bool, is_cheap:bool):
        self.name = name
        self.country = country
        self.is_reliable = is_realiable
        self.is_cheap = is_cheap
        self.__where_to_buy = "Go to afghanistan"

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
    
    def buy(self):
        try:
            print(f"In order to buy any of these guns without a permit you should go to {self.__where_to_buy}")
        except AttributeError:
            print("You are not allowed to know this")




auto_gun = Auto("AK", "russia", True, False, True)
auto_gun.sub_data()
auto_gun.main_data()

semi_gun = Semi("Glock", "Belgium", True, True, 15)
semi_gun.sub_data()
semi_gun.buy()



class Food:
    def __init__(self, name:str, is_healthy:bool, is_exoctic:bool)->None:
        self.name = name
        self.is_healthy = is_healthy
        self.is_exotic = is_exoctic

class Carbs(Food):
    def __init__(self, name:str, is_healthy:bool, is_exotic:bool, rich_in_iron:bool, rich_in_fiber:bool)->None:
        self.rich_in_iron = rich_in_iron
        self.rich_in_fiber = rich_in_fiber
        super().__init__(name, is_healthy, is_exotic)
    def show_data(self):
        print(f"Name: {self.name}, Healthy: {self.is_healthy}, Exotic: {self.is_exotic}, Is rich in iron {self.rich_in_iron}, Is rich in fiber: {self.rich_in_fiber} ")


my_food =Carbs("banana", True, True, True, True)
my_food.show_data()

