list1 = ["a","b","c"]
list2 = [1,2,3]

list3 = list1 + list2
print(list3)

print(" ********  ")
list3 = ["a","b","c"]
list4 = [1,2,3,4,5,6]

for x in list4:
    list3.append(x)
print(list3)

print(" ******* ")
list5 = ["a","b","c"]
list6 = [1,2,3,4,5,6]

list5.extend(list6)
print(list5)