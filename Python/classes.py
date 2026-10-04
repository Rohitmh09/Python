

class Human:
    def __init__ (self,gender,name= 'Bharat'):
        self.gender = gender
        self.name = name

class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color


h1 = Human('male','karan') #positional arguments 
print(h1.name)
print(h1.gender)

h2 = Human('female')
print(h2.name)
print(h2.gender)

c1 = Cat(color='blue',name = 'kavya') #names arguments position not matters when provide argumanet name
print(c1.name)
print(c1.color)