'''
Slicing a list in Python allows you to work with just a part of the list.
It also allows you to copy a list by not passing any parameter inside de slice[:]
'''
#4.10 Slices
fruits = ['apple', 'banana', 'watermelon', 'blueberry', 'uva','maracujá']
print(f'The firs three items in the list are: {fruits[:3]}.')
print(f'Three items from the middle of the list are: {fruits[3:6]}')
print(f'The las three items in the list are: {fruits[-3:]}')

#4.11 My Pizzas, Your Pizzas
    #From "4.1 Pizzas"
fav_pizzas = ['4 cheeses', 'peperoni', 'chicken']
friend_pizzas = fav_pizzas[:]
fav_pizzas.append('2 cheeses')
friend_pizzas.append('chocolate')

print(f'\nMy favorite Pizzas are:')
for pizza in fav_pizzas:
    print(pizza.title())
print(f"\nMy friend's favorite Pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())

#4.12 More Loops
mom_foods = ['pizza', 'falafel', 'carrot cake']
for food in mom_foods:
    print(f"One of my mom's favorite foods is: {food.title()}")
for food in mom_foods:
    print(f'This food exist somewhere: {food.title()}')