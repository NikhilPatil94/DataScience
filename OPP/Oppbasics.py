class Car:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

    def carinfo(self):
        print(self.Brand + self.Model)
    

Car1 = Car("Suzuki", "Breeza")
Car2 = Car("Suzuki", "WaganR")
Car3 = Car("Suzuki", "Swift")
Car4 = Car("Honda", "Elevete")
Car5 = Car("Hundai", "Cretra")

print(Car1.carinfo())
