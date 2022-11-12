#To determine how many items a tuple has, use the len() function: Lenght
thistuple = ("apple","chery","banana","Kiwi")
print(len(thistuple))

thistuple = ("Banana")
print(type(thistuple))


thistuple = (11)
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))

thistuple5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple5)

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
print("-"*20)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #negatif

print("-"*20)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

print("-"*20)


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
print("-"*20)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)

print("-"*20)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


print("-"*20)

thistuple = ("apple", "banana", "cherry")
y = ("orange")
thistuple += y

print(thistuple)


print("-"*20)

#del() : The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
