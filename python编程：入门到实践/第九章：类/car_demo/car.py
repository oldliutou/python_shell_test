'''
电池类 Battery
'''
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=85):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
'''
基类 Car
'''
class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        """汽车有油箱"""
        print("This car  need a gas tank!")
# my_new_car = Car('audi','A4',2016)
# print(my_new_car.get_descriptive_name())
#
# print(my_new_car.read_odometer())
#
# my_new_car.odometer_reading = 230
# print(my_new_car.read_odometer())
'''
    子类 ElectricCar()
'''
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = Battery()
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
# print(my_tesla.describe_battery())
print(my_tesla.battery_size.describe_battery())

print(my_tesla.fill_gas_tank())
# print(Car('a','b',2000).fill_gas_tank())

print(my_tesla.battery_size.get_range())