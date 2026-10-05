# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Manchester"] = "Irwell"
rivers["Birmingham"] = "Rea"
print(rivers)
print()
# Display all the keys
print(rivers.keys())
print()
# Display all the values
print(rivers.values())
print()
# Display all the key:value pairs, as tuples
key_value = list(rivers.items())
print(key_value)
# Delete an entry from the rivers database
rivers.pop("Leeds")
print(rivers)