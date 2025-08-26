#3.4 Guest List
people_to_have_a_dinner = ['yara', 'mãe', 'baus']   #Using for!
for person in people_to_have_a_dinner:
    print(f'{person.title()}, você gostaria de jantar comigo?')
print('-----------------------------------')

#3.5 Changing Guest List
people_to_have_a_dinner = ['yara', 'mãe', 'baus']
print(f'Que pena, o(a) {people_to_have_a_dinner[-1].title()} não irá ao jantar.')

    #Removing who can't go to dinner
cant_go = people_to_have_a_dinner.pop(-1)
    #Replacing
people_to_have_a_dinner.append('clóvis')

for person in people_to_have_a_dinner:
    print(f'{person.title()}, você gostaria de jantar comigo?')
print('-----------------------------------')

#3.6 More Guests
people_to_have_a_dinner = ['yara', 'mãe', 'baus', 'clóvis']
for person in people_to_have_a_dinner:
    print(f'{person.title()}, eu encontrei uma mesa maior, posso chamar mais pessoas!')
print('-----------------------------------')
    #Adding guests to the list
people_to_have_a_dinner.insert(0, 'igor 3k')        #Beginning of the list
people_to_have_a_dinner.insert(3, 'chris bumstead') #Middle
people_to_have_a_dinner.insert(6, 'biel')           #End

    #Inviting everyone
for person in people_to_have_a_dinner:
    print(f'{person.title()}, eu e mais um pessoal vamos sair para jantar, gostaria de vir com a gente?')
print('-----------------------------------')

#3.7 Shrinking Guest List
new_list_dinner = people_to_have_a_dinner           #IDK if this is necessary
for person in new_list_dinner:
    print(f'{person.title()}, infelizmente só conseguirei chamar duas pessoas para o jantar.')
print('-----------------------------------')
    #Removing guests with pop()
out_of_dinner = new_list_dinner.pop(-1) #Biel
print(f'{out_of_dinner.title()}, me desculpe mas não conseguirei te receber para o jantar. ')
out_of_dinner = new_list_dinner.pop(3)  #CBUM
print(f'{out_of_dinner.title()}, me desculpe mas não conseguirei te receber para o jantar. ')
out_of_dinner = new_list_dinner.pop(4)  #Baus
print(f'{out_of_dinner.title()}, me desculpe mas não conseguirei te receber para o jantar. ')
out_of_dinner = new_list_dinner.pop(2)  #Mãe
print(f'{out_of_dinner.title()}, me desculpe mas não conseguirei te receber para o jantar. ')
out_of_dinner = new_list_dinner.pop(0)  #Igor
print(f'{out_of_dinner.title()}, me desculpe mas não conseguirei te receber para o jantar. ')
print('-----------------------------------')
    #Telling who is still on dinner
for person in new_list_dinner:
    print(f'{person.title()}, você ainda está convidado(a) para o jantar.')
#Deleting list
del new_list_dinner[0]
del new_list_dinner[1]