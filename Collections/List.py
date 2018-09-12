#
thislist = ["apple", "banana", "cherry", "bot"]

#set new value to index
# thislist[0]="Orange", It will replace apple with Orange
# print(thislist[1])

#append , appends the item at the end
thislist.append("Blueberry")

#Insert , inserts with specified index
thislist.insert(3,"BlackBerry")

#The remove() method removes the specified item , pop() delete the last item in the List if you dont specify index
thislist.remove("BlackBerry")

#del deletes list if you dont specified index
# del thislist or del thislist(index) 

#you can create a List with constructor
thislist2=list(("ab","cd","de"))

#loop through
print("Items in the List")
for x in thislist:
    print(x)
print('length of thislist is',len(thislist))
print("")

print(thislist2)

#copy() copies one list to another
copiedList=thislist.copy()
print(copiedList)

#extend()  add list to another list at the end of list.
thislist.extend(thislist2)
print(thislist)
