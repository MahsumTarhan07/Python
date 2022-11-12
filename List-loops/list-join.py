list1 = ["a","b","c","d"]
list2 = [1,2,3,4]

for x in list2:
    list1.append(x)
print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a","b","c"]
list2 = [1,2,3]

list1.extend(list2)
print(list1)