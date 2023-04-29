
class Person():
    def __init__(self,fname,lname):
        self.firsName = fname
        self.lastName = lname
        print("Peson Created. ")
        
    def who_am_i(self):
        print("I am person class!")
    
    def eat(self):
        print("Eat")
        
    def hello(self):
        print("Welcome")
        
class Student(Person):
    def __init__(self,fname,lname,snumber):
        Person.__init__(self ,fname,lname)
        self.stdentNumber = snumber
        print("Student Created...")
      
    #override 
    def who_am_i(self):
        print("I am student")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
        
    def who_am_i(self):
        print(f"I am {self.branch} teacher. ")

p1 = Person("Ali","Cengiz")
s1 = Student("Cinar", "Kara", 1111)
t1 = Teacher("Mahsum","Tarhan","Math")


print(p1.firsName + ' ' + p1.lastName)
print(s1.firsName + ' ' + s1.lastName +" " + str(s1.stdentNumber))



t1.who_am_i()

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()

p1.hello()

