x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "KİWİ"
x = tuple(y)

print(x)

#append
thistuple = ("apple", "banana", "cherry","lemon","kiwi")
y1 = list(thistuple)
y1.append("ORANGE")
thistuple = tuple(y1)
print(thistuple)



thistuple2 = ("apple", "banana", "cherry","lemon","kiwi")
y = ("ORANGE2",)
thistuple2 +=y
print(thistuple2)
