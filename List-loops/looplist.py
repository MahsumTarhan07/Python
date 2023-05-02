

print("* #Print all items in the list, one by one:  *")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print("* Print all items by referring to their index number: *")


thislist2 = ["apple", "banana", "cherry","lemon"]
for i in range(len(thislist2)):
    print(thislist2[i])

print("* Print all items, using a while loop to go through all the index numbers *")

#Print all items, using a while loop to go through all the index numbers
thislist3 = ["apple", "banana", "cherry","lemon"]
i = 0
while i < len(thislist3):
    print(thislist3[i])
    i = i + 1

print("* short hand for loop that will print all items in a list: *")

#A short hand for loop that will print all items in a list:

thislist4 = ["apple", "banana", "cherry","lemon"]
[
    print(x) for x in thislist4
]
