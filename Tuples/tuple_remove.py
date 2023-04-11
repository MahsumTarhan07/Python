#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop(2)
print(thislist2)

#Remove the last item:
thislist3 = ["apple", "banana", "cherry","lemon"]
thislist3.pop()
print(thislist3)

#Remove the first item:
thislist4 = ["apple", "banana", "cherry"]
del thislist4[0]
print(thislist4)

#Delete the entire list:
thislist5 = ["apple", "banana", "cherry"]
del thislist5


#Clear the list content:
thislist6 = ["apple", "banana", "cherry"]
thislist6.clear()
print(thislist6)
