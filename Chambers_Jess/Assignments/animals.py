class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        print "walking..."
        self.health -= 1

        return self

    def run(self):
        print "running..."
        self.health -= 5

        return self

    def displayHealth(self):
        print "Name: ", self.name
        print "Health: ", self.health

        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
        self.name = name

    def pet(self):
        print 'petting...'
        self.health += 5
        
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
        self.name = name

    def fly(self):
        print 'flying...'
        self.health -= 10

        return self

    def displayHealth(self):
        print 'This is a Dragon'
        super(Dragon, self).displayHealth()

        return self

animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()

dog = Dog('dog')
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon('dragon')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
