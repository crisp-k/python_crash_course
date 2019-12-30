motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

    # modifying a list value
# motorcycles[0] = 'ducati'
# print(motorcycles)

    # appending to list
motorcycles.append('ducati')
# print(motorcycles)

    # creating empty list
# motorcycles = []
# print(motorcycles)

    # appending values to a list
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

    # inserting item into list
# motorcycles.insert(1, 'ducati')
#print(motorcycles)

    # deletes item from list for good
# del motorcycles[1]
#print(motorcycles)

    # removes item from list but stores it into a variable using .pop()
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

    # demonstrates the use of pop, and its ability to pop specific values using its index
# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}")

# first_owned = motorcycles.pop(1)
# print(f"The first motorcycle I owned was a {first_owned.title()}")

print(motorcycles)

    # demonstrates remove method, and use of a variable to remove
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
 