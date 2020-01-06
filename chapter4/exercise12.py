my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

# appending items to lists to show independence
my_foods.append('cannoli')
friends_foods.append('ice cream')


print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food.title())
