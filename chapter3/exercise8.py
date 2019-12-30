visit = ['London', 'Japan', 'Maine', 'Italy', 'Russia']
print("Original Order:")
print(visit)

print("\nTemp sorted:")
print(sorted(visit))

print("\nShowing original order is preserved:")
print(visit)

print("\nReverse temp sorted:")
print(sorted(visit, reverse=True))

print("\nShowing original order is preserved:")
print(visit)

print("\nReversing order")
visit.reverse()
print(visit)

print("\nReversing order again")
visit.reverse()
print(visit)

print("\nList sort:")
visit.sort()
print(visit)

print("\nReverse list sort:")
visit.sort(reverse=True)
print(visit)