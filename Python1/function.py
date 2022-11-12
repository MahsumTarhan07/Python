"""
def my_function():
    print("Hello from a function")

my_function()
""" 

""" 
def my_function(fname):
    print(fname + "Refsnes")

    my_function("Email")
    my_function("Tobaias")
    my_function("Linus")

"""

"""
def my_funtion(fname, lname):
    print(fname + " " + lname)
    
    my_funtion("Emil")

""" 
"""
def greet(name):
    print("Hello ", name)
greet('Steve') #calling function with argument
greet(123)

""" 
""" 
def greet(name:str):
    print("Hello", name)
greet('Steve') #calling function with string argument
greet(123)

""" 
""" 
def greet(name1, name2, name3):
    print("Hello ", name1 , "," , name2, "and", name3)
greet("Steve", "Bill" , "Yash")
""" 

""" 
def greet(*names):
    print("Hello " , names[0], ',', names[1] , 'and', names[2])
greet("Steve","Mayk","Yashu")
""" 

def greet(*names):
    i=0
    print("Hello ", end='')
    while len(names) > i:
        print(names[i],end=',')
        i+=1

greet('Steve', 'Bill', 'Yash') 
greet('Steve', 'Bill', 'Yash', 'Kapil', 'John', 'Amir') 


a = square(5)
print(a)
