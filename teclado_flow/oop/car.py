class Car:
    def __init__(self, brand, model, year):
        """инициализация атрибутов автомобиля"""
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def description(self):
        desc = str(self.year) + ' ' + self.brand + ' ' + self.model
        return desc.title()

    def show_mileage(self):
        print(f'Mileage is {self.mileage} km')

    def update_mileage(self, new_data):
        if new_data >= self.mileage:
            self.mileage = new_data
        else:
            print("Nope")

    def increase_mileage(self, new_data):
        self.mileage += new_data


car1 = Car('audi', 'a4', 2010)
print(car1.description())
# car1.mileage = 30
car1.update_mileage(454)
car1.increase_mileage(46)
car1.show_mileage()