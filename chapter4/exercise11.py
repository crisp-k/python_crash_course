pizzas = ['cheese', 'pepperoni', 'meat']
friends_pizzas = pizzas[:]

pizzas.append('fire hot')
friends_pizzas.append('supreme')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza.title()}")

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"\t{pizza.title()}")

