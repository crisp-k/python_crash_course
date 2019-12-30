letters = ['a', 'g', 'q', 'c', 't', 'x']
print(letters)

print(f"\nTitle case: {letters[0].title()}")

print("\nAppending a letter (y)")
letters.append('y')
print(letters)

print("\nInserting a letter (b; index: 1)")
letters.insert(1, 'b')
print(letters)

print("\nPopping a letter")
popped_letter = letters.pop(1)
print(popped_letter)

print("\nRemoving a letter (t)")
letters.remove('t')
print(letters)

print("\nSorting list in new list, preserving original list")
letters_sort = letters
letters_sort.sort
print(letters_sort)

print("\nReversing sort")
letters_sort.sort(reverse=True)
print(letters_sort)

print("\nTemp sort")
print(sorted(letters))

print("\nReversing list, then reversing again back to original order")
letters.reverse()
print(letters)
letters.reverse()
print(letters)

letters_len = len(letters)
print(f"\nLength of letters: {letters_len}")