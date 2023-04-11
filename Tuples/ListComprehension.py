

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)

#newlist = [expression for item in iterable if condition == True]
# newlist = [x for x in fruits if x != "apple"]

print("* With list comprehension you can do all that with only one line of code: *")
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newList2 = [x for x in fruits if "a" in x]
print(newList2)