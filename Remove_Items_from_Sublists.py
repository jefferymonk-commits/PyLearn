list_to_modify = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reference_list = [[1, 5], [8, 10]]

# Extract all elements from the reference_list into a flat set for efficient lookup
elements_to_remove = set()
for sublist in reference_list:
    for item in sublist:
        elements_to_remove.add(item)

# Iterate through list_to_modify and remove elements
new_list_to_modify = []
for sublist in list_to_modify:
    new_sublist = []
    for item in sublist:
        if item not in elements_to_remove:
            new_sublist.append(item)
    new_list_to_modify.append(new_sublist)

print(new_list_to_modify)