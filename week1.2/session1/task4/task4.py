# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)
# ---> {"tomato"}

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food)
# ---> union prints all the items combined in both the sets except duplicates

# Add an item to fruit
fruit.add("banana")
print(fruit)
# Remove an item from vegetables
vegetables.discard("potato")
print(vegetables)
# Find and display symmetric difference of the two sets
diff = fruit.symmetric_difference(vegetables)
print(diff)