'''
Tuple is a list that is considered "immutable", that means that it's values cannot be changed.
It is defined by using parentheses(), and can be accessed as if it was a list, with square brackets [].
If we try to change a value inside a tuple, Python will return an "TypeError" saying that a tuple cannot be changed.
In a creation of Tuples it must be defined by the presence of a comma(,), even if it'll have 1 parameter.

However, we can write over a tuple to have new values inside it.
'''

dimensions = (200, 50)
print(f'Original dimensions:')
for dimension in dimensions:
    print(dimension)
#Writing over a tuple
dimensions = (400, 100)
print('\nNew dimensions:')
for dimension in dimensions:
    print(dimension)
print('\n')
#4.13 Buffet:
buffet_items = ('rice', 'egg', 'chicken', 'bean', 'lettuce')
print("This are the Buffet Items:")
for item in buffet_items:
    print(item.title())
#Trying to modify the tuple:
#buffet_items[-1] = 'idk'
buffet_items = ('rice', 'egg', 'chicken', 'tomato', 'banana')
print('\nModified Buffet:')
for item in buffet_items:
    print(item.title())
