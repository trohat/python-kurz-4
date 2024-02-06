from abc import ABC, abstractmethod


class FuelStatus(ABC):

    @abstractmethod
    def show_fuel_status(self):

        
        """asfasdfasfas"""
        


class Car(FuelStatus):

    def __init__(self, color, model, engine_type, fuel_status: int):
        assert fuel_status >= 5, f"Min fuel or energy level must be 5 % of energy"

        self.color = color
        self.model = model
        self.engine_type = engine_type
        self.fuel_status = fuel_status

    @classmethod
    def default_model(cls):
        return cls("white", "fabia", "gasoline", 5)

    def __str__(self):
        return (
            f"{self.color}, {self.model}, {self.engine_type}, {self.fuel_status} L | %"
        )


class BusinessClass(Car, FuelStatus):
    def __init__(self):
        super().__init__("silver", "superb", "disel", 15)

    def show_fuel_status(self):
        if self.fuel_status <= 10:
            raise Exception("You need to fill a Diesel!")
        elif self.fuel_status > 100:
            raise Exception("You have a full tank!")
        return self.fuel_status


class SportCar(Car, FuelStatus):
    def __init__(self, speed_limit):
        super().__init__("yellow", "lambo", "gas", 50)
        self.speed_limit = speed_limit

    def show_fuel_status(self):

        if self.fuel_status <= 10:
            raise Exception("You need to fill a gasoline!")
        elif self.fuel_status > 100:
            raise Exception("You have a full tank!")
        return self.fuel_status


class ElectroCar(Car, FuelStatus):
    def __init__(self, battery_capacity: str):
        super().__init__("black", "tesla", "electro", 80)
        self.battery_capacity = battery_capacity

    def show_fuel_status(self):
        if self.fuel_status <= 30:
            raise Exception("You need to charge a battery!")
        elif self.fuel_status > 100:
            raise Exception("Battery is fully charged!")
        return self.fuel_status


skoda = BusinessClass()
lamborgini = SportCar(350)
tesla = ElectroCar("62kWh")


skoda.show_fuel_status()
lamborgini.show_fuel_status()
tesla.show_fuel_status()

cars = [skoda, lamborgini, tesla]
for car in cars:
    print(car)
