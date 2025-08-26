'''

'''

# cars = ['audi', 'bmw', 'chevrolet', 'honda', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
#
# #5.1 conditional tests
# caneta = 'staedler'
# print('\nSerá que caneta == "Faber Castel"? Eu acredito que é falso.')
# print(caneta == 'Faber Castel')
#
# print("Será que caneta == 'staedler'? Eu acredito que é verdade.")
# print(caneta == 'staedler')
#
# #5.2 More conditional tests
# perola = 'preta'
# print("\nA Pérola é branca? Eu digo que é falso.")
# print(perola == 'branca')
# print("A Pérola é preta? Eu digo que é verdadeiro.")
# print(perola == 'preta')
#
# gata_branca = 'Agatha'
# print("\nSerá que o nome da gata branca é agatha?")
# print(gata_branca.lower() == 'agatha\n')
#
# num1 = 20
# num2 = 80
# if num1 == 20:
#     print('Correto')
# elif num1 != 20:
#     print('Errado')
#
#
# requested_toppings = ['cogumelos', 'queijo extra']
#
# if 'cogumelos' in requested_toppings:
#     print("\nAdicionando cogumelos.")
# if 'peperoni' in requested_toppings:
#     print("Adicionando peperoni.")
# if 'queijo extra' in requested_toppings:
#     print("Adicionando queijo extra.")
#
# print("\nPizza pronta!")

#Utilizando For:
# requested_toppings = ['cogumelos', 'queijo extra', 'tomate']
#
# for requested_topping in requested_toppings:
#     print(f"Adicionando {requested_topping}.")
# print("\nFinalizando o seu pedido.")

# #E se a pizzaria ficar sem um dos itens?
# requested_toppings = ['cogumelos', 'queijo extra', 'tomate']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'cogumelos':
#         print("Desculpe, mas estamos sem cogumelos no momento.")
#     else:
#         print(f"Adicionando {requested_topping}.")
# print("\nFinalizando seu pedido.")

# #Checando se a lista de itens está vazia:
# requested_toppings = []
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adicionando {requested_topping}.")
#     print("\nFinalizando o seu pedido.")
# else:
#     print("Você tem certeza que quer uma pizza plana?")

# #Usando Multiplas Listas
# available_toppings = ['cogumelos', 'azeitonas', 'pimentão verde'
#                       'pepperoni', 'abacaxi', 'queijo extra', 'brócolis']
#
# requested_toppings = ['azeitonas', 'brócolis', 'alcaparra', 'abacaxi']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adicionando {requested_topping}.")
#     else:
#         print(f"Desculpe, mas não temos {requested_topping}.")
# print("\nPizza pronta!")