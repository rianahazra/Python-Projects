tuple1= (12,23,12,4512,12,12,12,2,32,532,35)
print(tuple1)
names=("Cat", 9, "Doe")
list1=["cat",79,"John"]
print(names,type(names))
print(list1,type(list1))
print("3rd element = ", names[2])
print("length =", len(names))
print(tuple1.count(12))
print(tuple1.index(4512))
print("index of all elements")
for element in tuple1:
    print(tuple1.index(element))
    
"""
#change first element in name to 50
names[1]=50
"""
"""
names=list(names)
names.reverse()
names=tuple(names)
print(names,type(names))
"""
