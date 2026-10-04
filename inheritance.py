
class BankBalance:
    def __init__(self,balance):
        self.balance = balance

    def depositAmount(self,amount):
        self.balance += amount


class BankService(BankBalance):

    def __init__(self,name,balance):
        self.name = name
        super().__init__(balance)

    def printInfo(self):
        print(f'Name: {self.name}, Balance: {self.balance}')



acc1 = BankService(name='karan',balance=9000)
acc1.depositAmount(400)
print(acc1.balance)
acc1.printInfo()


#Polymorphism 
    # => Method Overriding ==> Declaring method in subclass which is already 
                                # exists in parent class with same name and signature is called method overriding


class Dog:
    def sound(self):
        print('Animal sound')

class Cat(Dog):          #class Cat:
    def sound(self):
        print('Mew Cat sound')

    def callSuperMethod(self):
        super().sound()

an = Dog()
an.sound()

cat = Cat()
cat.sound()

animals = [Dog(),Cat()]

for animal in animals:
    animal.sound()
            
Dog.sound(cat)
cat.callSuperMethod()

    #method overloading


class AddInfinity:
    def calculate(self,*numbers):
        total =0
        for num in numbers:
            total += num
        print(f'total: {total}')

ad = AddInfinity()

ad.calculate(2,3,3,3,4)
ad.calculate(5,5)

# Duck typing 
# make sound method dosn't care about object is Dog or Cat it care about object has sound mehtod or not
def make_sounds(animal):
    animal.sound()

make_sounds(Dog())
make_sounds(Cat())


# Abstraction
# Hiding implementation details and exposing only what is necessary.

from abc import ABC, abstractmethod

class Vehical(ABC):

    @abstractmethod
    def start(self,name):
        pass

    def run(self):
        print('Car is running')

class Care(Vehical):
    def start(self,name):
        print(f'{name} Care Started')

c1 = Care()
c1.start('Ronine')
c1.run()

