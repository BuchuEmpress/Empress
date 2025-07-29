# a list is a collection of items
shopping_cart=["apples", "bread", "milk", "eggs"]
numbers = [1, 2, 3, 4, 5]
mixed_items=["Alice", 25, True, 3.14]
empty_cart=[]
print(f"Shopping cart: {shopping_cart}")
print(f"Numbers: {numbers}")
print(f"Mixed items: {mixed_items}")

# accessing the list items
fruits=["apple", "banana", "cherry", "date", "elderberry"]
print(f"The first fruit is: {fruits[0]}")
print(f"The second fruit is: {fruits[1]}")
print(f"The third fruit is: {fruits[2]}")
print(f"The fourth fruit is: {fruits[3]}")


print(f"First three fruits are: {fruits[0:3]}")
print(f"First fruit till end: {fruits[0:5]}")
print(f"Every second fruit: {fruits[::2]}")
print(f"Second fruit till the end: {fruits[-2]}")
print(f"Last fruit: {fruits[-1]}")

# modifying the list
groceries=["milk", "bread", "eggs"]
print(f"Original List is: {groceries}")

# adding a single item to the list
groceries.append("cheese")
print(f"After adding a single item, we have: {groceries}")

# adding multiple items to the list
groceries.extend(["apples", "bananas"])
print(f"After adding more than one item, we have: {groceries}")

# adding an item at a specific index
groceries.insert(1, "yogurt")
print(f"After adding \"Yogurt\" at point two, we have: {groceries}")

# changing an existing item
groceries[0]="Almond milk"
print(f"After changing \"Milk\" to \"Almond Milk\" we have: {groceries}")


# removing an item
groceries.remove("bread")
print(f"The list after removing bread: {groceries}")

removed_item= groceries.pop()       #remove and return the last item
print(f"Removed item: {removed_item}")  # this creates a holder for the removed item and displays it
print(f"After popping: {groceries}")

specific_item= groceries.pop(1)     #remove and return item at index one
print(f"Removed item at index one: {specific_item}")
print(f"Final List: {groceries}")

