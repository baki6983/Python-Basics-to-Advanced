# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values

carsDictionary={
    "name":"baki",
    "age":32,
    "city":"vaxjo"
}
xName=carsDictionary["name"]
carsDictionary["age"]=30
print(carsDictionary)

#adding item to dictionary
carsDictionary["color"]="brown"

#for loop
for x in carsDictionary.values():
    print(x)

#remove item in dictionary
del carsDictionary["age"]

print(carsDictionary)

# Lot of dictionary methods https://www.w3schools.com/python/python_dictionaries.asp
