# #6.4 Glossary 2 (cleaning the mess):
# python_glossary = {'list': 'Can store a set of data.',
#                    'dictionary': 'Can store a set of data with Key-Values.',
#                    'variable': 'Can store one piece of information.',
#                    'if': "Its an statement that can check for information."}
#
# print("This are the items on your Glossary:")
# for k, v in python_glossary.items():
#     print(f"{k.title()}: {v}")

# #6.5 Rivers:
# print("\nHere are 3 major rivers on Earth:")
# rivers = {'nilo': 'egypt',
#           'amazonas': 'amazonia',
#           'euphrates': 'western asia'}
# for river, location in sorted(rivers.items()):
#     print(f"The {river.title()} runs through {location.title()}!")
#
# # for river in rivers.keys():
# #     print(river.title())
# # for location in rivers.values():
# #     print(location.title())

# #6.6 Polling:
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# friends = ['ana', 'carlos', 'jen', 'paulo', 'edward']
# for person in friends:
#     if person not in favorite_languages:
#         print(f"Hey {person.title()}, you should take my poll!")
#     elif person in favorite_languages:
#         print(f"{person.title()}, thanks for taking my poll!")
#
# print("\nHere are the poll results:")
# for person, language in favorite_languages.items():
#     print(f"{person.title()}'s favorite language is {language.title()}.")
#
# print("\nAnd here are the languages that appeared on the poll:")
# for language in set(favorite_languages.values()):
#     print(f"{language.title()}.")

# #6.7 People:
# yrodrigues = {'first': 'yara',
#              'last': 'rodrigues',
#              'age': 23,
#              'born': 'são paulo'}
#
# jnarducci = {'first': 'joão',
#              'last': 'narducci',
#              'age': 22,
#              'born': 'são paulo'}
#
# scaetano = {'first': 'sivlia',
#              'last': 'caetano',
#              'age': 62,
#              'born': 'rio grande do sul'}
#
# people = [yrodrigues, jnarducci, scaetano]
#
# print("Here are the information about all people:")
# for person in people:
#     print(f"\nName: {person['first'].title()} {person['last'].title()}")
#     print(f"\tAge: {person['age']}")
#     print(f"\tBorn in: {person['born'].title()}")
#
# print("----------------------------------------------------------------------")
# #6.8 Pets:
# agatha = {'type': 'cat',
#         'name': 'agatha',
#         'age': 14,
#         'tutor': 'joão e silvia'}
# bebe = {'type': 'cat',
#         'name': 'bebê',
#         'age': 14,
#         'tutor': 'joão e silvia'}
# perola = {'type': 'cat',
#         'name': 'pérola',
#         'age': 14,
#         'tutor': 'joão e silvia'}
# nina = {'type': 'cat',
#         'name': 'nina',
#         'age': 13,
#         'tutor': 'yara e joão'}
#
# pets = [agatha, bebe, perola, nina]
#
# print("Here are the information about every Pet:")
#
# for pet in pets:
#     print(f"\nName: {pet['name'].title()}")
#     print(f"\tType: {pet['type'].title()}")
#     print(f"\tAge: {pet['age']}")
#     print(f"\tTutors: {pet['tutor'].title()}")

# #6.9 Favorite Places:
# favorite_places = {
#     'joão': ['academia', 'casa', 'parque'],
#     'yara': ['parque', 'livraria', 'minha casa'],
#     'silvia': ['casa', 'casa', 'casa']
# }
#
# for person, fav_place in favorite_places.items():
#     print(f"Os lugares favoritos de {person.title()} são:")
#     print(f"\t• {fav_place[0].title()}")
#     print(f"\t• {fav_place[1].title()}")
#     print(f"\t• {fav_place[2].title()}")

# #6.10 Favorite Numbers:
# fav_numbers = {'joão': [23, 76],
#                'yara': [45, 89],
#                'silvia': [118, 62],
#                'gabriel': [38,92],
#                'ana': [61,83]
#                }
# for name, fav_nums in fav_numbers.items():
#     print(f"{name.title()}'s favorite numbers are:")
#     print(f"\t{fav_nums[0]}, {fav_nums[1]}")

# #6.11 Cities:
# estoic_cities = {
#     'atenas': {
#         'name': 'atenas',
#         'country': 'grécia',
#         'curiosity': 'Onde a filosofia estoica foi fundada por Zenão de Cítio '
#                      'por volta de 300 a.C. Atenas foi um dos principais centros do estoicismo.'
#     },
#     'roma': {
#         'name': 'roma',
#         'country': 'itália',
#         'curiosity': 'Muitos estóicos importantes, como Sêneca e Epicteto, viveram e ensinaram em '
#                      'Roma, fazendo dela um centro de atividade estoica durante o Império Romano.'
#     },
#     'rodes': {
#         'name': 'rodes',
#         'country': 'grécia',
#         'curiosity': 'A ilha de Rodes foi o local onde Panécio de Rodes, um dos mais influentes '
#                      'filósofos estóicos, viveu e desenvolveu suas ideias.'
#     }
# }
#
# for city, info in estoic_cities.items():
#     print(f"\nInformações sobre uma das cidades que gerou um dos mais memoráveis estóicos:")
#     city_name = f"{info['name']}"
#     country = f"{info['country']}"
#     curiosity = f"{info['curiosity']}"
#
#     print(f"\tCidade: {city_name.title()}")
#     print(f"\tPaís em que está localizada: {country.title()}")
#     print(f"\t{curiosity}")
