# aliens = []
#
# #Creating 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# #Mesmo que os aliens tenham as mesmas caracteristicas, o Python os vê como objetos individuais.
# #Podemos alterá-los separadamente:
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
#
# #Shows first 5 aliens:
# print("Here is a list with the 5 first aliens:")
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# #Show how many aliens have been created:
# print(f"\nTotal number of aliens is: {len(aliens)}.")

# #List inside a Dictionary:
# pizza = {'crust': 'thin',
#          'toppings': ['mushrooms', 'extra cheese'],
#          }
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping.title())

#Dictionary inside a Dictionary:
users = {
    'joão': {
        'first': 'joão',
        'last': 'narducci',
        'hobby': 'workout',
        'job': 'student'

    },

    'yara': {
        'first': 'yara',
        'last': 'rodrigues',
        'hobby': 'read',
        'job': 'itaú ux'
    },

    'silvia': {
        'first': 'silvia',
        'last': 'caetano',
        'hobby': 'watch tv',
        'job': 'mom'
    }
}

for username, userinfo in users.items():
    print(f"{username.title()}:")
    full_name = f"{userinfo['first']} {userinfo['last']}"
    job = userinfo['job']
    hobby = userinfo['hobby']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tJob: {job.title()}")
    print(f"\tHobby: {hobby.title()}")