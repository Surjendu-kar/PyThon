# how to create Dictionaries using list
keys = ['Surjo','RAhul','Raj']
value = ['JS','python','Java']

data = dict(zip(keys,value)) 
print(data)

data['Taj'] = 'CS'
print(data)

del data['Taj']
print(data)