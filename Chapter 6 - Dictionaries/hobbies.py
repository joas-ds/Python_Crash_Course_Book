# #É comum utilizarmos dicionários para guardar valores de um determinado assunto.
# hobbies = {'joão': 'treinar',
#            'yara': 'ler',
#            'silvia': 'ver TV'}
# # hobbie_j = hobbies['joão'].title()
# # print(f"O hobby do João é {hobbie_j}.")
# 
# #Loop:
# for name, hobby in hobbies.items():
#     print(f"\nO hobby favorito do(a) {name.title()} é {hobby}.")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# #O método keys também serve pra checar se alguma chave não está no dicionário:
# if 'erin' not in favorite_languages.keys():
#     print(f"Erin, please take our poll!")

#Alterando a ordem de dicionários:
#sorted() function:
# hobbies = {'joão': 'treinar',
#            'yara': 'ler',
#            'silvia': 'ver TV'}
# for name in sorted(hobbies.keys()):
#     print(f"{name.title()} esta é uma ordem aleatória.")

#Looping through all Values:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages appeared on the list:")
#Using the set() collection to NOT REPEAT the languages on the dictionary
for language in set(sorted(favorite_languages.values())):
    print(language.title())

#Hobby
users_hobbies = {'joão': ['treinar', 'ler', 'assistir YT', 'aprender'],
           'yara': ['ler', 'assistir anime','andar de patins']}

for name, hobbies in users_hobbies.items():
    print(f"\nOs hobbies favoritos de {name.title()} são:")
    for hobby in hobbies:
        print(f"\t{hobby.title()}")