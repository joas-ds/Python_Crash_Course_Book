''' NOTES:
Sorting with sort() method. It organizes the list by alphabetical order.
    -> It cannot be undone, the sort() method organizes PERMANENTLY.
    -> It can be organized in reverse alphabetical order, by using the parameter "reverse=True" - sort(reverse=True)
Sorting with sorted() method. It also organizes a list by alphabetical order.
    -> Does not affect the original order of a list.
Printing a list in Reverse. The reverse() method only invert the order of the list.
    -> This method changes the list permanently, but can be undone, by using reverse() to the same list again.
len() function, shows the length of a list. Very useful.
'''
#3.8 Seeing The World
places_to_vist = ['canada', 'united states', 'london', 'tokyo', 'japan']
print(places_to_vist)
print(sorted(places_to_vist))
print(places_to_vist)
print(sorted(places_to_vist, reverse=True))
print(places_to_vist)
places_to_vist.reverse()
print(places_to_vist)
places_to_vist.reverse()
print(places_to_vist)
places_to_vist.sort()
print(places_to_vist)
places_to_vist.sort(reverse=True)
print(places_to_vist)

#3.9 Dinner Guests:
# Using code from "guest_list.py"
people_to_have_a_dinner = ['yara', 'mãe', 'baus']
print(f'{len(people_to_have_a_dinner)} is the amout of people in the dinner.')

#3.10 Every Function
#3.11 Intentional Error
places_to_vist.sort(reverse=False)
print(places_to_vist)
del places_to_vist[-1]
#print(places_to_vist[4]) - error
print(places_to_vist[-1])