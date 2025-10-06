

#To find a value in a nested tuple within a list in Python, you can use a combination of loops, list comprehensions, or built-in functions like filter. Below are three approaches:

nested_list = [(1, 2), (3, 4), (5, 6)]
target = 4

for tup in nested_list:
    if target in tup:
        print(f"Found {target} in tuple {tup}")
        break
else:
    print(f"{target} not found")



data = [("apple", (1, 2)), ("banana", (3, 4)), ("cherry", (5, 6))]

# Find a specific value, e.g., 4
target = 4
found = False

for item in data:
    if target in item[1]:  # Check if the value exists in the nested tuple
        found = True
        print(f"Found {target} in {item}")
        break

if not found:
    print(f"{target} not found.")

