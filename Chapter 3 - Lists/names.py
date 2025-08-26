#3.1 Names
friend_names = ['Biel', 'Mene', 'Emily', 'Mateus']
print(friend_names[0])          #Printing friend names one by one.
print(friend_names[1])
print(friend_names[2])
print(friend_names[3])
print('-----------------------------------')
for friend in friend_names:     #Printing friends names using for.
    print(friend)
print('-----------------------------------')

#3.2 Greetings
print(f'{friend_names[0]} é um dos meus amigos.')   #Printing a phrase with each friend name one by one.
print(f'{friend_names[1]} é um dos meus amigos.')
print(f'{friend_names[2]} é um dos meus amigos.')
print(f'{friend_names[3]} é um dos meus amigos.')
print('-----------------------------------')
for friend in friend_names:                         #Printing a phrase with each friend using for.
    print(f'{friend} é um dos meus amigos.')
print('-----------------------------------')

#3.3 Your Own List
transports = ['honda civic', 'moto foda', 'a pé']
print(f'Eu gosto bastante de dirigir o {transports[0].title()} que a gente tem.')
print(f'Eu adoraria ter uma {transports[1]} um dia!')
print(f'Eu gosto muito de andar {transports[-1]} para refletir sobre meus pensamentos.')