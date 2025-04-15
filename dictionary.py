# Example of using a dictionary in Python

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Adding a new key-value pair
my_dict["profession"] = "Engineer"
print("Updated Dictionary:", my_dict)

# Modifying an existing value
my_dict["age"] = 26
print("Modified Dictionary:", my_dict)

# Removing a key-value pair
del my_dict["city"]
print("Dictionary after deletion:", my_dict)

# Iterating through the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "name" in my_dict:
    print("Key 'name' exists in the dictionary.")

# Getting a value with a default
profession = my_dict.get("profession", "Not specified")
print("Profession:", profession)