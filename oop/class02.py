
#class

class Person:

    adress = "No information'"
    
    #consturcator
    def __init__(self, name, year):
      self.name = name
      self.year = year
      
    # instance metods    
    def intro(self):
      print("Hello there, I am " + self.name)
    
    def calculatorAge(self):
        return 2019 - self.year

p1 = Person("Muzaffer",1999)
p2 = Person("Yağmur",2000)

p1.intro()
p2.intro()

print(f'name: {p1.name} and age: {p1.calculatorAge()}')
print(f'name: {p2.name} and age: {p2.calculatorAge()}')


