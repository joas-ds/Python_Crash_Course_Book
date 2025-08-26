# #7.1 Rental Car:
# user_car = str(input("Which type of car would you like to rental? "))
# print(f"Ok, let me see if I can find you a {user_car.title()}.")

# #7.2 Restaurant Seating:
# qtde_people = int(input(f"Hello and Welcome to our restaurant!"
#       f"\nBefore you come in, please tell us how many people are coming to eat? "))
#
# if qtde_people > 8:
#     print(f"Ok! You guys will have to wait for a table.")
# else:
#     print(f"Right. Your table is ready, please come in!")

# #7.3 Multiple of Ten:
# number = int(input("Enter a number and I'll tell if it is a multiple of 10 or not. "))
#
# if number % 10 == 0:
#     print(f"The number {number} is a multiple of 10.")
# else:
#     print(f"The number {number} it's not a multiple of 10.")

# #7.4 Pizza Toppings:
# active = True
# toppings = []
#
# print("\nSeja Bem-Vindo a nossa pizzaria!")
#
# prompt1 = "Por gentileza, informe o 1° item que deseja em sua pizza. "
# prompt2 = "Por gentileza, informe o 2° item que deseja em sua pizza. "
# prompt3 = "Por gentileza, informe o último item que deseja em sua pizza. "
#
# while active:
#
#     if len(toppings) == 0:
#         item = input(prompt1)
#         toppings.append(item)
#     elif len(toppings) == 1:
#         item = input(prompt2)
#         toppings.append(item)
#     elif len(toppings) == 2:
#         item = input(prompt3)
#         toppings.append(item)
#     elif len(toppings) == 3:
#         active = False
#
# print(f"\nCerto, seu pedido estará pronto em 30 minutos. "
#       f"\nOs itens escolhidos foram: "
#       f"\n\t• {toppings[0].title()}"
#       f"\n\t• {toppings[1].title()}"
#       f"\n\t• {toppings[2].title()}")

# #7.5 Movie Tickets:
#
# ticket_price = 0
#
# print(f"Welcome to our Movie Theater!")
# age = int(input("In order to buy a ticket, please informe your age.\n "))
#
# while True:
#     if age < 3:
#         ticket_price = 0
#     elif age <= 12:
#         ticket_price = 10
#     else:
#         ticket_price = 15
#     break
#
# print(f"Your enter is US${ticket_price},00."
#       f"\nHave a nice session.")

#7.6 Three Exits:
# Already did it

# #7.7 Infinity:
# print("I'M GONNA JUMP INTO THE VOID!!")
#
# keep_or_not = input("IF YOU WANT TO KEEP ME SAY IT NOW."
#                     "\nWill you save him? (Type 'Yes' or 'No'). ")
#
# if keep_or_not == 'Yes':
#     print("Thank you, you saved me.")
# else:
#     mets = 0
#     while mets < 1:
#         print("AAAAAAAAHHHHHHHHHHHHH")