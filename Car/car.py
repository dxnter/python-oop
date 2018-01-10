'''
Car Arguments

Price - As an integer
Speed - Top speed as an integer
Fuel - Integer 1 - 100 representative of the percentage of fuel
Mileage - As an integer
'''
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
            
        if fuel == 100:
            self.fuel_message = 'Full'
        elif 50 <= fuel <= 100:
            self.fuel_message = 'Kind of Full'
        elif 0 <= fuel <= 49:
            self.fuel_message = 'Not Full'
        elif fuel < 0:
            self.fuel_message = 'You cannot have a negative fuel integer!'
        self.display_all()

    def display_all(self):
        print 'Price:',self.price
        print 'Speed:',self.speed
        print 'Fuel:',self.fuel_message
        print 'Mileage:',self.mileage
        print 'Tax:',self.tax

car1 = Car(15000, 50, 100, 25)
car2 = Car(3000, 25, 45, 30)
car3 = Car(170000, 95, 22, 29)
car4 = Car(45000, 75, 75, 45)
car5 = Car(1000, 15, 0, 15)
car6 = Car(95000, 75, 100, 34)