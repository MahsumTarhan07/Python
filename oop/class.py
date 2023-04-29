
#class

class Person:

    adress = "No information'"
    
    #consturcator
    def __init__(self, name, year):
      self.name = name
      self.year = year
      print("init metodu çalıştı...")
      
    #metods
    
    #object

p1 = Person("Muzaffer",1999)
p2 = Person("Murat",2000)

#updateing
p1.name = "Mustafa"

#accessing object attributes
print(f'name: {p1.name} year: {p1.year}  adress: {p1.adress}')
print(f'name: {p2.name} year: {p2.year}  adress: {p2.adress}')


print(type(p1))
print(type(p2))

