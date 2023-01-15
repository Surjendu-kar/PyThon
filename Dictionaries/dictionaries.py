# Dictionaries are used to store data values in key:value pairs.
# we can create dictionaries set
data = {1:'Rahul',2:'surjo',4:'Raj'}  
print(data)
print(data[4])
print(data.get(1,'not found'))
print(data.get(3,'not found')) #if we not found the key then we show any message

data['year'] = '2003'; # add new key 
print(data)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["year"])
print(thisdict.get("model"))

#how to get only keys
print(thisdict.keys())

#how to get values
print(thisdict.values())
