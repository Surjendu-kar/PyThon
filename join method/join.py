names = ["surjo","rahul","raj","noddy"]
print(names)

#convert list to str
print(''.join(names)) #but type is list
print(type(new_num))

#another process 

new_num = ''
for i in names:
    new_num = i + new_num # type is str

print(new_num)
print(type(new_num))