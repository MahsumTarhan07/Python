#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange","mongo","kiwi"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) 


def myFunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 45]
thislist.sort(key=myFunc)
print(thislist)


#reverse() methos reverses the current sorting order of the elements.

tthislist = ["banana", "Orange", "Kiwi", "cherry"]
tthislist.reverse(),
print(tthislist)