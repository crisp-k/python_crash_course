dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# to show tuples cannot be changed
#dimensions[0] = 250

# showing how tuples print similarly to lists
print(dimensions)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# 'modifying' a tuple by redefining the entire tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)