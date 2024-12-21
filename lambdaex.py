#double=lambda x: x*2
#print(double(3))

# numbers=[1,2,3,4,5]
# double_nums=list(map(lambda x:x*2, numbers))
# print(double_nums)

# list=["Harshith", "Shaun", "Anaya", "Bob", "Derek", "Alex", "Yohanty"]
# sort1=sorted(list, key=lambda list: len(list))
# print(sort1)

# celsius=[50,10,80,900,20,30]
# farenheit=list(map(lambda x: x * 9/5 + 32, celsius)) 
# print(farenheit)

# number=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x: x%2==0, number))
# print(even)

# list1=["Harshith", "Shaun", "Anaya", "Bob", "Derek", "Alex", "Yohanty"]
# five=list(filter(lambda x: len(x)>5, list1))
# print(five)

emails=["abc@gmail.com", "cat@gmail.org", "dog@gmail.com", "snake@yahoo.org", "pig@gmail.com"]
a=list(filter(lambda x: x.endswith(".com"), emails))
print(a)

words=["cat","dog","hello","eye"]
check=list(filter(lambda x: x==x[::-1], words))
print(check)