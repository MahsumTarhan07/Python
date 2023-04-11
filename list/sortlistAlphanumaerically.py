
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print("* Sort the list numerically *")

thislist2 = [100,23,12,48,41,2]
thislist2.sort()
print(thislist2)

print("* Sort the list descending *")
thislist3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist3.sort(reverse= True)
print(thislist3)

thislist4 = [100,23,60,48,41,24]
thislist4.sort(reverse= False)
print(thislist4)


print("*****************")
def myFun(n):
    return abs(n -50)

thislist5 = [100, 50, 65, 82, 23]
thislist5.sort(key=myFun)
print(thislist5)

print("*****************")
thislist6 = ["banana","Orange","Kiwi","Chersy"]
thislist6.sort()
print(thislist6)

print("* Reverse the order of the list items: *")

thislist7 = ["banana","Orange","Kiwi","Chersy","Lemon"]
thislist7.reverse()
print(thislist7)
