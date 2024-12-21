amount=int(input("Enter amount of shopping items"))
shoppingList=[]
for i in range (0,amount):
    item=input("Enter the shopping items")
    shoppingList.append(item)
prizelist=["apple", "banana", "grapes", "mangoes"]
shoppingList=shoppingList+prizelist
shoppingList.sort()
print(shoppingList)
#shoppingList.reverse()

#shoppingList.remove("dog")

'''
shopping_list=["apple",3, "strawberries",5, "dragonfruit",2]
shopping_list.append("mangoes")
print(shopping_list)
shopping_list.insert(6,"banana")
print(shopping_list)
shopping_list.extend(["grapes","apple"])
print(shopping_list)
'''
