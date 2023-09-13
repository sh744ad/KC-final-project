print("Welcome to the Simple Shopping Cart")
list_item=[]
item1=input("enter item 1:")
item2=input("enter item 2:")
item3=input("enter item 3:")
list_item.append(item1)
list_item.append(item2)
list_item.append(item3)
print(list_item)
print(len(list_item))
print(list_item)
item4=int(input("enter one of the items to delet"))
list_item.pop(item4)
print(list_item)
item5=int(input("enter value to the items"))


