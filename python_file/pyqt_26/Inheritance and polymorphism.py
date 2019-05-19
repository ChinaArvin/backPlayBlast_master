class Animal(object):
    def run(self):
        print('Animal is runing..')

class Dog(Animal):
    def run(self):
        print('Dog is runing..')
class Cat(Animal):
    pass

class Tortoise(Animal):
    def run(self):
        print('Tortoise is runing slowly..')

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()
run_twice(Tortoise())