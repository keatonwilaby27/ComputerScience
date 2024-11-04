
for i in range(0,10):  
    print(i)

top_foods = ["eggs", "chicken", "mac and cheese"]

for food in top_foods:
    print(food)
groceries = ["milk", "egg", "bread", "apples"]
purchased_item = input("what item did you buy\n")
for grocery in groceries:
    if grocery == purchased_item.lower():
        print(grocery + "checked off the list")
        groceries.remove(grocery)

print(groceries)