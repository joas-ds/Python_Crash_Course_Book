#Quando tentamos puxar um valor em um dicionário, usando [], e esse valor não existe é gerado um erro.
#Podemos evitar isso, usando o método get():
# alien_0 = {'color': 'green', 'speed': 'slow'}
#
# point_value = alien_0.get('points', 'No point value assigned yet.')
# print(point_value)

#6.1 Person:
yara_info = {'first_name': 'yara',
             'last_name': 'rodrigues',
             'age': 23,
             'city': 'são paulo'}
print(f"A {yara_info['first_name'].title()} tem {yara_info['age']} anos e mora em {yara_info['city'].title()}.\n")

#6.2 Favorite Numbers:
fav_numbers = {'joão': 33,
               'yara': 22,
               'silvia': 118,
               'gabriel': 66,
               'ana': 24}
print(fav_numbers['joão'])
print(fav_numbers['yara'])
print(fav_numbers['silvia'])
print(fav_numbers['gabriel'])
print(fav_numbers['ana'])

#6.3 Glossary:
python_glossary = {'list': '\nCan store a set of data.',
                   'dictionary': '\nCan store a set of data with Key-Values.',
                   'variable': '\nCan store one piece of information.',
                   'if': "\nIts an statement that can check for information."}

print(python_glossary['list'])
print(python_glossary['dictionary'])
print(python_glossary['variable'])
print(python_glossary['if'])