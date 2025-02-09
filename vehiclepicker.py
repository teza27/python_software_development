class Vehicles:
    def __init__(self, manufacturer: str, model: str, year: int):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
    def get_details(self):
        print(f"{self.manufacturer} {self.model} {self.year} model")

class Car(Vehicles):
    def __init__(self, manufacturer: str, model: str, year: int, num_door: int):
        super().__init__(manufacturer, model, year)
        self.num_door = num_door
    def get_details(self):
        print(f"The automobile {self.model} is made by {self.manufacturer} in the year {self.year} and has {self.num_door} doors")

class Motorcycle(Vehicles):
    def __init__(self, manufacturer: str, model: str, year: int, top_speed: float):
        super().__init__(manufacturer, model, year)
        self.top_speed = top_speed
    def get_details(self):
        print(f"The automobile {self.model} is made by {self.manufacturer} in the year {self.year} and a top speed of {self.top_speed}")
        

class Truck(Car):
    def __init__(self, manufacturer: str, model: str, year: int, num_door, cargo_capacity: float):
        super().__init__(manufacturer, model, year, num_door)
        self.cargo_capacity = cargo_capacity
    def get_details(self):
        print(f"The automobile {self.model} is made by {self.manufacturer} in the year {self.year} and has {self.num_door} doors and cargo capacity of {self.cargo_capacity}")
        
    
sedan_car = Car("Toyota", "Corolla", 2013, 4)
sedan_car.get_details()

power_bike = Motorcycle("BMW", "GT", 2013, "350MPH")
power_bike.get_details()

excation_truck = Truck("CAT", "Howo", 2010, 2, 40.5)
excation_truck.get_details()