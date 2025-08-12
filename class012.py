# 1. Tuple Basics
cities = ("London", "Paris", "Tokyo")
print("Cities tuple:", cities)
print("Length of cities tuple:", len(cities))

# 2. One-Item Tuple
country = ("Canada",)
print("Type of country:", type(country))
not_a_tuple = ("Canada")  # without comma
print("Type without comma:", type(not_a_tuple))

# 3. Accessing Tuple Items
animals = ("dog", "cat", "rabbit", "parrot")
print("First animal:", animals[0])
print("Last animal (negative index):", animals[-1])
print("Items from index 1 to 3:", animals[1:4])

# 4. Modifying Tuples
colors = ("red", "blue", "green")
colors_list = list(colors)
colors_list[1] = "yellow"
colors = tuple(colors_list)
print("Updated colors tuple:", colors)

# 5. Adding & Removing Items in Tuples
devices = ("laptop", "tablet", "phone")

# Adding item
devices_list = list(devices)
devices_list.append("smartwatch")
devices = tuple(devices_list)

# Removing item
devices_list.remove("tablet")
devices = tuple(devices_list)
print("Updated devices tuple:", devices)

# 6. Unpacking Tuples
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter")
inner1, inner2, *others = planets
print("Inner1:", inner1)
print("Inner2:", inner2)
print("Others:", others)

# 7. Loop Through Tuples
sports = ("football", "basketball", "tennis")

# Using for loop
for sport in sports:
    print(sport)

# Using range(len(...))
for i in range(len(sports)):
    print(sports[i])

# 8. Joining and Multiplying Tuples
tuple1 = ("x", "y")
tuple2 = (10, 20)
joined_tuple = tuple1 + tuple2
print(joined_tuple)

multiplied_tuple = tuple1 * 3
print(multiplied_tuple)

# 9. Basic Set Operations
languages = {"Python", "Java", "C++"}
languages.add("JavaScript")
languages.update({"Go", "Ruby"})
print(languages)

# 10. Removing Items from Sets
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")  # Removes banana
print(fruits)

fruits.discard("grape")  # No error if grape not present
print(fruits)
