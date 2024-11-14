# Dictionary is a type of collection like list 




# Dictionary is a type of collection like list
# A lsit is a colelciton of items in a sequence
# A Dictionary is different
# Dictionaries store data in key-value pairs
# You can retreive data quickly by using a unique key
# instead of retreving it by index (position)

#Example
# Lists use brackets, dictionaries use braces
Evan = {
    "name": "Evan",
    "age": 16,
    "city": "St. Michael",
    "pets": 0,
    
}
# Each key must be unique

# Retreiving values from a dictionary

print(Evan["age"])

# .get allows you to retreive a value without erroring
# when the key doesn't exist
# The second parameter is what is given if value is not found
print(Evan.get("height"))
print(Evan.get("weight", "fortnite"))

# You can add values to a dictionary
Evan["country"] = "USA"

# You can modify values
Evan["age"] = 16

print(Evan)

# Remove entries
Evan.pop("pets")

# Iterate through a dictionary using a for loop
for key, value in Evan.items():
    print(key + ": " + str(value))

# Dictionary functions
print(Evan.keys())   #returns all keys
print(Evan.values()) #returns all values
print(Evan .items())  #returns all pairs
print(Evan.clear())  #removes all items from the dict