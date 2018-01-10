class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.name,'Health:',self.health

class Dog(Animal):
    health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
        print self.health

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print self.name,'Health:',self.health,'I am a dragon'
        

animal1 = Animal('Roxanne', 100)
animal1.walk().walk().walk().run().run().display_health()