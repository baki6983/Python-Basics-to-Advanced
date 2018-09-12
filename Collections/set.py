# A set is a collection which is unordered(prints randomly) and unindexed. In Python sets are written with curly brackets

fruitsSet={"apple","banana","cherry"}
print(fruitsSet)

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

# you cant do that(fruitsSet[0])

#for loop , you can check if item in the set like below
print("apple" in fruitsSet)

# you cant change the value , but you can add new item in the set
fruitsSet.add("corn")

# Add multiple items to a set, using the update() method
fruitsSet.update(["blueberry","blackberry","mango"])
for item in fruitsSet:
    print(item)

# To remove an item in a set, use the remove(), or the discard() method , only diff is discrd will throw exception like remove

fruitsSet.remove("diefh") # this will throw exception
fruitsSet.discard("sidnfgifg") # this will not throw exception , but tells name "" not defined.

# You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# The clear() method empties the set, its clear the data but Set will be there

# The del keyword will delete the set completely , it completely deletes set with data , if you tried to print , throws exception

# It is also possible to use the set() constructor to make a set.

# There are lot of methods in the Set , please go to https://www.w3schools.com/python/python_sets.asp
