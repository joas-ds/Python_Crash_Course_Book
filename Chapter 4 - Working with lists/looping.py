'''
Looping through a List
    -> It allows to do the same task with every item on a list.
    -> uses "for".
    -> If the line after the for loop is no indented, it will cause an "IdentationError" and the for loop is not
    going to run.
    -> If the second line into the for loop is not indented, the code will run, but it won't do what we expect.
    -> Because there is a single line inside the for loop Python can run the program.
'''
#4.1 Pizzas
fav_pizzas = ['4 cheeses', 'peperoni', 'chicken']
for pizza in fav_pizzas:
    print(f'I like {pizza} pizza.')
print('I like to eat pizza, sometimes.\n')

#4.2 Animals
mammals_animals = ['cat', 'dog', 'whale']
for animal in mammals_animals:
    print(f'A {animal.title()} is a great animal.')
print('Did you know that all of these animals are mammals?\n')

'''
The range() function allows you to generate a series of numbers.
    -> eg: for value in range(1,6):
                print(value)
    -> this will print the numbers 1 to 5.
    -> The function range() also allows you to pass only ONE value, 
        and it will start counting from 0 to the given value
    -> You can MAKE a LIST of numbers converting the results of the function range() directly into a list,
        using the list() function (eg.: list(range(0,101))
    -> You can pass a THIRD value to the range() function, and it'll skip the amount that has been given when
        counting. (eg.: list(range(0,26,2))
'''

numbers = list(range(2,26,2))
print(numbers)
#Creating empty list, doing a for() with range() and storing it to the list.
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print('\n')
#print(sum(squares))     #sum just 4fun.
#print(max(squares))
#Doing the same thing above, but in just one line ---> List Comprehension:
multiples_of_3 = [value*3 for value in range(1,10)]
print(multiples_of_3)
print('\n')

#4.3 Counting to Twenty
for number in range(1,21):
    print(number)
#4.4 One Million
million = [number for number in range(1_000_001)]   #USING LIST COMPREHENSION!!!!!
print(million)
#4.5 Summing a Million
print(min(million))
print(max(million))
print(sum(million))
#4.6 Odd Numbers
numbers_2 = list(range(1,21,2))
print(numbers_2)
#4.7 Threes
multiples_of_3 = [value*3 for value in range(3,31)] #List Comprehension
print(multiples_of_3)
#4.8 Cubes
cubes = []     #Longer way:
for value in range(1,11):
    cubes.append(value**3)
print(cubes)
#4.9 Cube Comprehesion!!!
cubes_comprehesion = [value**3 for value in range(1,11)]
print(cubes_comprehesion)